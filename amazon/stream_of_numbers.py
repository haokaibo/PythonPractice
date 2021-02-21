"""
given stream numbers
..........t....t...
get the highest product of 3 numbers() -> answer

time: O(n)
space: O(3)
"""


class Node:
    def __init__(self, val, pre=None, nxt=None):
        self.val = val
        self.pre = pre
        self.nxt = nxt

    def __str__(self):
        return str(self.val)


class LinkedList:
    def __init__(self, capacity):
        self.head = Node('head')
        self.capacity = capacity
        temp = self.head
        for i in range(capacity):
            new_node = Node(0, pre=temp)
            temp.nxt = new_node
            temp = new_node

    def add_node(self, val):
        temp = self.head.nxt
        index = 0

        while temp is not None:
            if temp.val < val:
                new_node = Node(val, temp.pre, temp)
                temp.pre.nxt = new_node
                temp.pre = new_node
                index += 1
                while index < self.capacity and temp is not None:
                    temp = temp.nxt
                    index += 1
                if index == self.capacity:
                    temp.pre.nxt = None
                    temp = None
                break
            temp = temp.nxt
            index += 1


class MinHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.heap = [0] * capacity
        self.max_product = 0

    def add(self, val):
        self.heap.append(val)
        current = self.capacity
        parent = current // 2
        while self.heap[current] < self.heap[parent]:
            self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
            current = parent
            parent = current // 2
        self.heap = self.heap[1:]

    def peek(self):
        return self.heap[0]


class Solution:
    """
    Time: O(log(k) * n) + O(1)
    """

    def getHighestProductOf3Numbers(self, nums: [], k=3):
        if nums is None or len(nums) < k:
            return None
        cache = MinHeap(k)
        max_product = 1
        for i in nums:
            min_val = cache.peek()
            if min_val < i:
                if min_val > 0:
                    max_product = max_product // min_val
                cache.add(i)
                max_product = max_product * i

        return max_product

    """
    Time: O(n*3)
    """

    def getHighestProductOf3Numbers_bad(self, nums: []):
        if nums is None or len(nums) < 3:
            return None
        capacity = 3
        cache = LinkedList(capacity)

        for i in nums:
            cache.add_node(i)

        curr = cache.head.nxt
        max_product = None
        index = 0
        while curr is not None:
            if index == 0:
                max_product = curr.val
            else:
                max_product = max_product * curr.val
            index += 1
            curr = curr.nxt
        return max_product


solution = Solution()
print(solution.getHighestProductOf3Numbers([3, 2, 1]))
print(solution.getHighestProductOf3Numbers([1, 2, 3]))
print(solution.getHighestProductOf3Numbers([]))
print(solution.getHighestProductOf3Numbers([1]))
print(solution.getHighestProductOf3Numbers([1, 2]))
# import heapq
#
# a = [7, 2, 3, 5]
# heapq.heapify(a)
# print(a)
# heapq.heappushpop(a, 8)
# print(a)
