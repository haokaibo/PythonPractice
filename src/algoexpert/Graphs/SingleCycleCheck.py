def hasSingleCycle(array):
    """
    Question Description
    -------------------
    You are given an array of integers where each integer represents the
    number of steps to jump forward (positive) or backward (negative) in
    the array. When jumping, the array is treated as circular, so jumping
    past the last element wraps around to the first element and vice
    versa.

    Write a function that determines whether starting at the first element
    (index 0) and following the jumps, you will visit every element in the
    array exactly once and return to index 0. If you do, the array has a
    single cycle; return True. Otherwise, return False.

    Example:
        array = [2, 3, 1, -4, -4, 2]
        -> True (0 -> 2 -> 3 -> 5 -> 1 -> 4 -> 0, visiting every element
           exactly once and returning to 0)

        array = [1, -1, 1, -1]
        -> False (returns to 0 before visiting all elements)

    Time Complexity: O(n)
        We traverse at most n nodes since we stop after visiting n elements.
        Each step performs O(1) work to compute the next index.

    Space Complexity: O(1)
        We only use a constant amount of extra space (counters and an index),
        no additional data structures proportional to the input size.
    """

    num_visited = 0
    current_idx = 0
    n = len(array)

    while num_visited < n:
        # 在还没跳满 N 次前，如果提前回到了起点，说明形成了局部小环
        if num_visited > 0 and current_idx == 0:
            return False

        num_visited += 1
        # 计算下一次跳跃的索引
        current_idx = get_next_idx(current_idx, array)

    # 跳跃 N 次后，必须恰好回到起点 0
    return current_idx == 0


def get_next_idx(current_idx, array):
    n = len(array)
    jump = array[current_idx]
    next_idx = (current_idx + jump) % n
    # Python 的 % 运算符会自动处理负数余数，但在其它语言中需要防范负数索引：
    return next_idx if next_idx >= 0 else next_idx + n
