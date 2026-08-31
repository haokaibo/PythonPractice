"""
LeetCode 75. Sort Colors [Medium]

Given an array nums with n objects colored red, white, or blue, sort them
in-place so that objects of the same color are adjacent, with the colors in
the order red, white, and blue. We use the integers 0, 1, and 2 to represent
the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input:  nums = [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]

Example 2:
Input:  nums = [2, 0, 1]
Output: [0, 1, 2]

Constraints:
- n == nums.length
- 1 <= n <= 300
- nums[i] is either 0, 1, or 2.

Follow up: Could you come up with a one-pass algorithm using only constant
extra space?

Solution 1 (counting sort, two-pass, in-place):
    Count occurrences of 0, 1, 2, then overwrite the array.
    Time : O(n)
    Space: O(1) extra

Solution 2 (Dutch National Flag / three-way partition, one-pass, in-place):
    Single pass with three pointers (low, mid, high). This is the
    one-pass / O(1) extra space solution requested in the follow-up.
    Time : O(n)
    Space: O(1) extra

Both satisfy the "in-place" requirement of the problem.
"""


def sort_colors_counting(arr):
    """Two-pass in-place solution using counts."""
    if not arr:
        return arr

    counts = [0, 0, 0]
    for c in arr:
        counts[c] += 1

    idx = 0
    for color, cnt in enumerate(counts):
        for _ in range(cnt):
            arr[idx] = color
            idx += 1
    return arr


def sort_colors_dutch_flag(arr):
    """One-pass in-place solution using the Dutch National Flag algorithm."""
    low = mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


if __name__ == "__main__":
    # Demo: both functions are in-place, so the original list is mutated.
    colors = [2, 0, 2, 1, 1, 0]
    sort_colors_counting(colors)
    print(colors)  # [0, 0, 1, 1, 2, 2]

    colors = [2, 0, 2, 1, 1, 0]
    sort_colors_dutch_flag(colors)
    print(colors)  # [0, 0, 1, 1, 2, 2]

    # Edge cases
    print(sort_colors_counting([]))        # []
    print(sort_colors_dutch_flag([2, 2]))  # [2, 2]
    print(sort_colors_dutch_flag([0]))     # [0]