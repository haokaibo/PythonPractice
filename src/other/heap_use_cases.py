# -*- coding: utf-8 -*-
"""
堆 / 优先队列 (Priority Queue) 典型应用场景实现
================================================

包含以下用例：
1. 优先队列 —— 任务调度器 / 定时器事件循环
2. Dijkstra 最短路径算法
3. Prim 最小生成树算法
4. Top K 问题（海量数据 Top-K）
5. 双堆法动态维护中位数
6. 堆排序（原地，O(1) 额外空间）
7. 多路归并（外部排序场景）

依赖：仅使用标准库 heapq / itertools / dataclasses
"""

import heapq
import itertools
import random
from dataclasses import dataclass, field
from typing import Any, List, Tuple, Iterator, Dict


# ============================================================
# 1. 优先队列：任务调度 / 定时器事件循环
# ============================================================
class PriorityTaskScheduler:
    """
    基于堆的任务调度器。
    - 数字越小优先级越高（与操作系统调度惯例一致）。
    - 使用自增计数器 counter 作为 tie-breaker，
      解决优先级相同时任务对象无法比较、以及保证 FIFO 稳定性的问题。
    - 支持"取消任务"（惰性删除：标记 + 弹出时跳过）。
    """

    REMOVED = "<removed-task>"  # 取消标记

    def __init__(self):
        self._heap: List[list] = []
        self._entry_finder: Dict[str, list] = {}
        self._counter = itertools.count()  # tie-breaker，保证同优先级先进先出

    def add_task(self, task_id: str, priority: float):
        if task_id in self._entry_finder:
            self.cancel_task(task_id)
        count = next(self._counter)
        entry = [priority, count, task_id]
        self._entry_finder[task_id] = entry
        heapq.heappush(self._heap, entry)

    def cancel_task(self, task_id: str):
        entry = self._entry_finder.pop(task_id)
        entry[-1] = self.REMOVED  # 惰性删除，不真正从堆里移除（避免 O(n) 重建堆）

    def pop_task(self) -> str:
        while self._heap:
            priority, count, task_id = heapq.heappop(self._heap)
            if task_id is not self.REMOVED:
                del self._entry_finder[task_id]
                return task_id
        raise IndexError("scheduler 中没有待执行任务")

    def is_empty(self) -> bool:
        return not self._entry_finder


@dataclass(order=True)
class TimerEvent:
    """定时器事件：按到期时间 due_time 排序，最早到期的事件在堆顶。"""
    due_time: float
    seq: int = field(compare=True)
    name: str = field(compare=False)
    callback: Any = field(compare=False, default=None)


class EventLoop:
    """
    简化版事件循环 / 定时器：
    每次 tick 只处理堆顶（最近到期）的事件，
    模拟 asyncio / Node.js 定时器堆的核心思想。
    """

    def __init__(self):
        self._heap: List[TimerEvent] = []
        self._seq = itertools.count()

    def call_later(self, delay: float, name: str, callback=None):
        heapq.heappush(self._heap, TimerEvent(due_time=delay, seq=next(self._seq), name=name, callback=callback))

    def run_until_empty(self, current_time: float = 0.0):
        """假设时间从 0 开始单调推进，依次触发所有到期事件。"""
        while self._heap:
            event = heapq.heappop(self._heap)
            current_time = max(current_time, event.due_time)
            print(f"[EventLoop] t={current_time:.1f} 触发事件: {event.name}")
            if event.callback:
                event.callback()


# ============================================================
# 2. Dijkstra 最短路径算法（邻接表 + 最小堆）
# ============================================================
def dijkstra(graph: Dict[Any, List[Tuple[Any, float]]], source: Any) -> Dict[Any, float]:
    """
    graph: {node: [(neighbor, weight), ...]}
    返回 source 到各节点的最短距离字典。
    时间复杂度 O((V + E) log V)。
    """
    dist: Dict[Any, float] = {node: float("inf") for node in graph}
    dist[source] = 0
    visited = set()
    heap = [(0, source)]  # (当前已知最短距离, 节点)

    while heap:
        d, u = heapq.heappop(heap)
        if u in visited:
            continue  # 惰性删除：跳过堆中过期（非最新）的记录
        visited.add(u)

        for v, w in graph.get(u, []):
            new_dist = d + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

    return dist


# ============================================================
# 3. Prim 最小生成树算法（邻接表 + 最小堆）
# ============================================================
def prim_mst(graph: Dict[Any, List[Tuple[Any, float]]], start: Any) -> Tuple[List[Tuple[Any, Any, float]], float]:
    """
    graph: {node: [(neighbor, weight), ...]}（无向图，两端都需要有边）
    返回 (MST 的边列表[(u, v, w)], 总权重)。
    """
    visited = {start}
    edges = [(w, start, v) for v, w in graph.get(start, [])]
    heapq.heapify(edges)

    mst_edges: List[Tuple[Any, Any, float]] = []
    total_weight = 0.0

    while edges and len(visited) < len(graph):
        w, u, v = heapq.heappop(edges)
        if v in visited:
            continue  # 两端都已在树中，跳过（避免成环）
        visited.add(v)
        mst_edges.append((u, v, w))
        total_weight += w

        for nxt, nw in graph.get(v, []):
            if nxt not in visited:
                heapq.heappush(edges, (nw, v, nxt))

    return mst_edges, total_weight


# ============================================================
# 4. Top K 问题：使用大小为 K 的堆，O(n log K)
# ============================================================
def top_k_largest(nums: List[float], k: int) -> List[float]:
    """
    维护一个大小为 K 的最小堆：
    - 堆里始终是当前遍历过的元素中最大的 K 个；
    - 堆顶是这 K 个里最小的一个，作为淘汰基准。
    时间复杂度 O(n log K)，空间复杂度 O(K)。
    """
    if k <= 0:
        return []
    heap = nums[:k]
    heapq.heapify(heap)

    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)  # 弹出堆顶 + 压入新元素，一次操作完成

    return sorted(heap, reverse=True)


def top_k_frequent_words(words: List[str], k: int) -> List[Tuple[str, int]]:
    """海量数据高频词统计场景：先统计词频，再用堆取 Top K。"""
    from collections import Counter
    counter = Counter(words)
    # nlargest 内部对 n << len(iterable) 的情况会用堆优化，等价于维护大小为 k 的堆
    return heapq.nlargest(k, counter.items(), key=lambda x: x[1])


# ============================================================
# 5. 双堆法（对顶堆）动态维护数据流中位数
# ============================================================
class MedianFinder:
    """
    - small：最大堆（Python heapq 只支持最小堆，取负数模拟最大堆），存较小的一半
    - large：最小堆，存较大的一半
    - 维持不变量：len(small) == len(large) 或 len(small) == len(large) + 1
    插入 O(log n)，取中位数 O(1)。
    """

    def __init__(self):
        self.small: List[float] = []  # 存负数，模拟最大堆
        self.large: List[float] = []  # 最小堆

    def add_num(self, num: float):
        heapq.heappush(self.small, -num)
        # 保证 small 堆顶 <= large 堆顶
        heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def find_median(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0


# ============================================================
# 6. 堆排序（原地排序，O(1) 额外空间，不依赖 heapq）
# ============================================================
def heap_sort(arr: List[float]) -> List[float]:
    """
    经典原地堆排序实现（手写，不调用 heapq，体现"原地"和空间复杂度 O(1)）：
    1) 建大顶堆 O(n)
    2) 依次将堆顶（当前最大值）与末尾元素交换，缩小堆范围后下沉调整 O(n log n)
    """
    n = len(arr)

    def sift_down(heap: List[float], start: int, end: int):
        """对 [start, end) 范围内、以 start 为根的子树做下沉调整。"""
        root = start
        while True:
            child = 2 * root + 1
            if child >= end:
                break
            if child + 1 < end and heap[child] < heap[child + 1]:
                child += 1
            if heap[root] < heap[child]:
                heap[root], heap[child] = heap[child], heap[root]
                root = child
            else:
                break

    # 建堆：从最后一个非叶子节点开始，从下往上下沉
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, i, n)

    # 依次弹出堆顶（最大值）放到数组末尾
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end)

    return arr


# ============================================================
# 7. 多路归并（外部排序场景）：合并多个已排序文件/序列
# ============================================================
def k_way_merge(sorted_iterables: List[Iterator]) -> Iterator:
    """
    使用 heapq.merge 完成多路归并：
    内部维护一个大小为 K（K = 已排序序列个数）的最小堆，
    每次从堆顶取出当前最小值，时间复杂度 O(N log K)（N 为元素总数）。
    这是 heapq.merge 的等价手写实现，用于展示原理；
    生产环境直接用 heapq.merge(*iterables) 即可。
    """
    heap = []
    iterators = [iter(it) for it in sorted_iterables]

    # 初始化：每个文件/序列取出第一个元素入堆
    for idx, it in enumerate(iterators):
        try:
            value = next(it)
            heapq.heappush(heap, (value, idx))
        except StopIteration:
            pass

    while heap:
        value, idx = heapq.heappop(heap)
        yield value
        try:
            next_value = next(iterators[idx])
            heapq.heappush(heap, (next_value, idx))
        except StopIteration:
            pass


def merge_sorted_files_demo(chunks: List[List[float]]) -> List[float]:
    """模拟"多个已排序小文件外部合并为一个大文件"的场景。"""
    return list(k_way_merge([iter(chunk) for chunk in chunks]))


# ============================================================
# ------------------------- Demo / 测试 -------------------------
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("1. 任务调度器 (Priority Queue)")
    print("=" * 60)
    scheduler = PriorityTaskScheduler()
    scheduler.add_task("低优先级日志任务", priority=5)
    scheduler.add_task("高优先级告警任务", priority=1)
    scheduler.add_task("中等优先级备份任务", priority=3)
    scheduler.cancel_task("低优先级日志任务")
    while not scheduler.is_empty():
        print(" 执行任务:", scheduler.pop_task())

    print("\n1b. 定时器事件循环 (Timer / Event Loop)")
    loop = EventLoop()
    loop.call_later(3.0, "刷新缓存")
    loop.call_later(0.5, "心跳检测")
    loop.call_later(1.2, "发送通知")
    loop.run_until_empty()

    print("\n" + "=" * 60)
    print("2. Dijkstra 最短路径")
    print("=" * 60)
    graph_dijkstra = {
        "A": [("B", 4), ("C", 1)],
        "B": [("A", 4), ("C", 2), ("D", 5)],
        "C": [("A", 1), ("B", 2), ("D", 8)],
        "D": [("B", 5), ("C", 8)],
    }
    print(dijkstra(graph_dijkstra, "A"))

    print("\n" + "=" * 60)
    print("3. Prim 最小生成树")
    print("=" * 60)
    graph_prim = {
        "A": [("B", 2), ("C", 3)],
        "B": [("A", 2), ("C", 1), ("D", 4)],
        "C": [("A", 3), ("B", 1), ("D", 5)],
        "D": [("B", 4), ("C", 5)],
    }
    mst_edges, total = prim_mst(graph_prim, "A")
    print("MST 边:", mst_edges, "| 总权重:", total)

    print("\n" + "=" * 60)
    print("4. Top K 问题")
    print("=" * 60)
    random.seed(42)
    big_data = [random.randint(0, 10000) for _ in range(100000)]
    print("Top 5 最大值:", top_k_largest(big_data, 5))
    words = "苹果 香蕉 苹果 橙子 苹果 香蕉 葡萄 苹果 香蕉".split()
    print("Top 2 高频词:", top_k_frequent_words(words, 2))

    print("\n" + "=" * 60)
    print("5. 双堆法动态维护中位数")
    print("=" * 60)
    mf = MedianFinder()
    stream = [5, 15, 1, 3, 8, 7, 9, 2]
    for x in stream:
        mf.add_num(x)
        print(f" 插入 {x:>3} 后，当前中位数 = {mf.find_median()}")

    print("\n" + "=" * 60)
    print("6. 堆排序")
    print("=" * 60)
    unsorted_arr = [12, 3, 7, 1, 9, 5, 14, 2, 8]
    print("排序前:", unsorted_arr)
    print("排序后:", heap_sort(unsorted_arr))

    print("\n" + "=" * 60)
    print("7. 多路归并（模拟外部排序）")
    print("=" * 60)
    file_chunks = [
        [1, 4, 9, 20],
        [2, 3, 15],
        [0, 5, 6, 7, 100],
    ]
    print("各已排序小文件:", file_chunks)
    print("归并后的大文件:", merge_sorted_files_demo(file_chunks))
