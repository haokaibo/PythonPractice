"""
Subarray Sort

Write a function that takes in an array of integers and returns the
indices of the smallest subarray that, if sorted, would make the entire
array sorted in ascending order.

A subarray is defined as a contiguous block of values in the array.

If the array is already sorted, the function should return [-1, -1].

Example 1:
    Input:  array = [1, 2, 4, -2, 5, 7, 8]
    Output: [0, 3]
    Explanation: Sorting the subarray [1, 2, 4, -2] yields [-2, 1, 2, 4],
    and the entire array becomes [-2, 1, 2, 4, 5, 7, 8], which is sorted.

Example 2:
    Input:  array = [2, 4, 5, 7, 3, 6, 8]
    Output: [1, 5]
    Explanation: Sorting the subarray [4, 5, 7, 3, 6] makes the whole array
    sorted.

Example 3:
    Input:  array = [1, 2, 3, 4, 5]
    Output: [-1, -1]
"""

from typing import List


def subarraySort(array: List[int]) -> List[int]:
    """
    Optimized Solution: Time: O(n), Space: O(1)

    Strategy:
    1. Scan the array to find all elements that are "out of order" — i.e.
       elements that violate the ascending ordering with respect to at
       least one neighbor. Track the minimum and maximum values among
       those out-of-order elements (minOutOfOrder / maxOutOfOrder).
    2. If no out-of-order element exists, the array is already sorted and
       we return [-1, -1].
    3. Otherwise, find the left boundary: the first index whose value is
       greater than minOutOfOrder (that value must be part of the
       subarray to sort). Likewise find the right boundary: the last
       index whose value is less than maxOutOfOrder.
    4. Return [leftBoundary, rightBoundary].

    Why it works:
    - Any out-of-order element must be moved, so the subarray must
      contain at least one of them.
    - The smallest out-of-order element defines the left boundary —
      every index to its left whose value exceeds it is also out of place.
    - The largest out-of-order element defines the right boundary —
      every index to its right whose value is smaller than it is also
      out of place.

    Time complexity  : O(n) — three linear passes over the array.
    Space complexity : O(1) — only a constant number of scalar variables.
    """
    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")

    # Edge case: a 0- or 1-element array is always sorted
    if len(array) < 2:
        return [-1, -1]

    # 1. Find the min and max among all out-of-order elements
    for i in range(len(array)):
        num = array[i]
        if isOutOfOrder(i, num, array):
            minOutOfOrder = min(minOutOfOrder, num)
            maxOutOfOrder = max(maxOutOfOrder, num)

    # 2. If the array was already fully sorted, return the sentinel value
    if minOutOfOrder == float("inf"):
        return [-1, -1]

    # 3. Find the left boundary: first index whose value > minOutOfOrder
    subarrayLeft = 0
    while minOutOfOrder >= array[subarrayLeft]:
        subarrayLeft += 1

    # 4. Find the right boundary: last index whose value < maxOutOfOrder
    subarrayRight = len(array) - 1
    while maxOutOfOrder <= array[subarrayRight]:
        subarrayRight -= 1

    return [subarrayLeft, subarrayRight]


def isOutOfOrder(i: int, num: int, array: List[int]) -> bool:
    """
    Return True if the element at index `i` is out of order in what
    should be a non-decreasing array.
    - The first element is out of order if it is greater than its right
      neighbor.
    - The last element is out of order if it is less than its left
      neighbor.
    - Any middle element is out of order if it is greater than its right
      neighbor OR less than its left neighbor.
    """
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]
    return num > array[i + 1] or num < array[i - 1]


# Example usage and test cases
if __name__ == "__main__":
    # Test case 1: AlgoExpert-style example
    array1 = [1, 2, 4, -2, 5, 7, 8]
    result1 = subarraySort(array1)
    print(f"Test 1 - Array: {array1}")
    print(f"Subarray sort: {result1} (expected: [0, 3])")
    print()

    # Test case 2: Middle dip
    array2 = [2, 4, 5, 7, 3, 6, 8]
    result2 = subarraySort(array2)
    print(f"Test 2 - Array: {array2}")
    print(f"Subarray sort: {result2} (expected: [1, 5])")
    print()

    # Test case 3: Already sorted
    array3 = [1, 2, 3, 4, 5]
    result3 = subarraySort(array3)
    print(f"Test 3 - Array: {array3}")
    print(f"Subarray sort: {result3} (expected: [-1, -1])")
    print()

    # Test case 4: Two elements swapped at the end
    array4 = [1, 2, 3, 6, 4, 5]
    result4 = subarraySort(array4)
    print(f"Test 4 - Array: {array4}")
    print(f"Subarray sort: {result4} (expected: [3, 3])")
    print()

    # Test case 5: Entire array out of order (reverse sorted)
    array5 = [5, 4, 3, 2, 1]
    result5 = subarraySort(array5)
    print(f"Test 5 - Array: {array5}")
    print(f"Subarray sort: {result5} (expected: [0, 4])")
    print()

    # Test case 6: Single element — already sorted
    array6 = [42]
    result6 = subarraySort(array6)
    print(f"Test 6 - Array: {array6}")
    print(f"Subarray sort: {result6} (expected: [-1, -1])")
