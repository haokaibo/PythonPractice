"""
LeetCode 154. Find Minimum in Rotated Sorted Array II [Hard]

Suppose an array of length n sorted in ascending order is rotated between
1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
  - [4,5,6,7,0,1,2] if it was rotated 4 times.
  - [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], ..., a[n-1]] 1 time results in
the array [a[n-1], a[0], a[1], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the
minimum element of this array.

You must decrease the overall operation steps as much as possible.

Example 1:
Input:  nums = [1,3,5]
Output: 1

Example 2:
Input:  nums = [2,2,2,0,1]
Output: 0

Example 3:
Input:  nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 4:
Input:  nums = [4,5,6,7,0,1,2]
Output: 0

Example 5:
Input:  nums = [1,1,1,1]
Output: 1

Constraints:
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- nums is a sorted rotated array that may contain duplicates.

Note: This is the same problem as LeetCode 153, but the array may contain
duplicates. That forces the algorithm to degrade from O(log n) to O(n) in
the worst case (when nums[mid] == nums[right] and we cannot tell which half
holds the minimum).
"""

"""
Solution (Binary Search on the rotation point, with duplicate handling):

The rotated array has two sorted halves. At any index mid:
  - If nums[mid] < nums[right], the right half [mid..right] is sorted and
    non-decreasing, so the minimum lies in [left..mid]. Set right = mid.
  - If nums[mid] > nums[right], the rotation point (minimum) is strictly
    to the right of mid, so set left = mid + 1.
  - If nums[mid] == nums[right], we cannot decide. Shrink the window by
    one (right -= 1). This may discard the minimum, but only when there
    is a duplicate of it elsewhere in [mid..right], so the answer is
    preserved.

Loop invariant: nums[0..left-1] are all >= the true minimum, and
nums[right+1..n-1] are all >= the true minimum. Loop terminates when
left == right, which is the rotation point itself.

Time : O(log n) average, O(n) worst case (all elements equal).
Space: O(1)
"""

class Solution:
    def helper(self, nums, begin, end):
        if begin == end:
            return nums[begin]
        
        mid = (begin + end) // 2

        if mid == begin and nums[end]<nums[mid]:
            return nums[end]
        # print(f'nums={nums}, begin={begin}, mid={mid}, end={end}')
        # print(f'nums[{begin}]={nums[begin]}, nums[{mid}]={nums[mid]}, nums[{end}]={nums[end]}')

        if nums[begin] <= nums[mid] <= nums[end]:
            return nums[begin]
        elif nums[begin] > nums[mid]:
            # check the min between begin and mid
            return self.helper(nums, begin, mid)
        else:
            # check the min betwen mid and end
            return self.helper(nums, mid, end)

    def findMin(self, nums):
        if not nums:
            return None
        return self.helper(nums, 0, len(nums)-1)

    def findMin_iter(self, nums):
        """Iterative version of findMin.

        Compare nums[mid] with nums[right] to decide which half contains
        the minimum (rotation point). When nums[mid] == nums[right] we
        cannot tell, so shrink the window by one.

        Time : O(log n) average, O(n) worst case (all elements equal).
        Space: O(1)
        """
        if not nums:
            return None

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                # Right half [mid..right] is sorted and non-decreasing,
                # so the minimum is at mid or to its left. Keep mid.
                right = mid
            elif nums[mid] > nums[right]:
                # Rotation point is strictly to the right of mid.
                left = mid + 1
            else:
                # nums[mid] == nums[right]: cannot decide. Shrink right.
                # Safe because the duplicate of nums[mid] elsewhere in
                # [mid..right] preserves the answer.
                right -= 1
        return nums[left]


if __name__ == "__main__":
    # Cases with unique elements: both versions work correctly.
    cases = [
        ([3,4,5,1,2], 1),
        ([3,1,2], 1),
        ([4, 5, 1, 2], 1),
        ([], None),
        ([2, 1], 1),
        ([2, 3, 4, 5, 1], 1),
    ]
    print('--- cases where both versions run ---')
    for case in cases:
        min_recursive = Solution().findMin(case[0])
        min_iterative = Solution().findMin_iter(case[0])
        ok_r = "ok" if min_recursive == case[1] else "failed"
        ok_i = "ok" if min_iterative == case[1] else "failed"
        print(f'rec={ok_r} iter={ok_i} | {case[0]} -> expected {case[1]}')

    # Edge cases that expose an infinite recursion in the original helper:
    # when nums[begin] <= nums[mid], the else branch keeps mid unchanged,
    # so (mid, end) == (begin, end) and there is no progress.
    edge_cases = [
        ([1], 1),
        ([1, 2], 1),
        ([1, 2, 3, 4, 5], 1),  # not rotated
    ]
    print('--- edge cases: iterative version only ---')
    for case in edge_cases:
        min_iterative = Solution().findMin_iter(case[0])
        ok_i = "ok" if min_iterative == case[1] else "failed"
        print(f'iter={ok_i} | {case[0]} -> expected {case[1]}')

    # LeetCode 154 specific: arrays with duplicates.
    # Iterative version is the recommended approach here because the
    # recursive helper only compares nums[begin] vs nums[mid] and has
    # no way to deal with duplicates that cross the midpoint.
    dup_cases = [
        ([1, 3, 5],             1),
        ([2, 2, 2, 0, 1],       0),
        ([3, 1, 2],             1),
        ([3, 3, 1, 3],          1),
        ([1, 1, 1, 1],          1),
        ([1, 1, 1, 0, 1],       0),
        ([1, 0, 1, 1, 1],       0),
        ([5, 5, 5, 5, 1, 5],    1),
    ]
    print('--- duplicate cases: iterative version only ---')
    for case in dup_cases:
        min_iterative = Solution().findMin_iter(case[0])
        ok_i = "ok" if min_iterative == case[1] else "failed"
        print(f'iter={ok_i} | {case[0]} -> expected {case[1]}')