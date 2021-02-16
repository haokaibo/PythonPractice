"""
Given an array which represent the x coordinates for a histogram chart,
find the largest area in the histogram.
"""
from collections import deque


class Stack:
    def __init__(self):
        self.deque = deque()

    def push(self, val):
        self.deque.append(val)

    def pop(self):
        return self.deque.pop()

    def peek(self):
        if self.empty():
            return None
        return self.deque[-1]

    def empty(self):
        return len(self.deque) == 0


def get_largest_area_in_histogram(arr):
    """
    Optimized implementation which took O(n) to implement.
    """
    max_area = 0
    if arr is None or len(arr) == 0:
        return 0

    stack = Stack()

    for i, val in enumerate(arr):
        if stack.empty() or arr[stack.peek()] < val:
            stack.push(i)
        else:
            while not stack.empty() and arr[stack.peek()] > val:
                curr_max_index = stack.pop()
                width = i - curr_max_index
                height = arr[curr_max_index]
                max_area = max(width * height, max_area)
            stack.push(i)

    while not stack.empty():
        curr_max_index = stack.pop()
        if stack.empty():
            width = len(arr)
        else:
            width = len(arr) - stack.peek() - 1
        height = arr[curr_max_index]
        max_area = max(width * height, max_area)
    return max_area


arrs = [
    [1, 2, 3, 4, 5, 5, 3, 2],
    [1, 1],
    [2, 1, 2],
    [1, 2, 1],
    [1, 2, 2, 1],
    [1, 3, 3, 1],
    [1, 3, 1, 1],
    [1, 3, 5, 5, 4, 10]
]
for a in arrs:
    print(f"{a}.max_area={get_largest_area_in_histogram(a)}")


#
#
# Bad implementation which takes O(n^2) to finish.


def find_largest_area_in_histogram(arr):
    max_area = 0
    if arr is None or len(arr) == 0:
        return max_area

    num_dic = dict()
    for i, v in enumerate(arr):
        if v not in num_dic:
            num_dic[v] = i
            max_area = max(v, max_area)
        else:
            # check all the previous bars are greater and equals to me
            all_greater_or_equals_to_me = True
            for j in range(num_dic[v] + 1, i):
                if arr[j] < v:
                    all_greater_or_equals_to_me = False
                    break

            if all_greater_or_equals_to_me:
                max_area = max((i - num_dic[v] + 1) * v, max_area)

    return max_area

# print(find_largest_area_in_histogram(arr))
