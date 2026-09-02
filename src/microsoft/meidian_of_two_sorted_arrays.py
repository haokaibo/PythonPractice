"""
LeetCode 4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
    nums1 = [1, 3], nums2 = [2]
    median is 2.0

Example 2:
    nums1 = [1, 2], nums2 = [3, 4]
    median is (2 + 3) / 2 = 2.5

Constraints:
    0 <= len(nums1) <= 1000
    0 <= len(nums2) <= 1000
    -10^6 <= nums1[i], nums2[i] <= 10^6
    nums1 and nums2 cannot both be empty.

Approach: binary search on the shorter array to find a partition i in nums1
and j in nums2 such that:
    left part  = nums1[0..i-1] + nums2[0..j-1]
    right part = nums1[i..m-1] + nums2[j..n-1]
    |left| - |right| is 0 (even) or 1 (odd)
    every left element <= every right element

Let L1, R1, L2, R2 be the boundary values (with sentinels for empty halves):
    median (odd)  = max(L1, L2)
    median (even) = (max(L1, L2) + min(R1, R2)) / 2

Time complexity: O(log(min(m, n))).
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2:
            return None

        # Always binary-search the shorter array to keep the loop O(log min(m, n)).
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        # half = number of elements on the left side of the cut.
        half = (m + n + 1) // 2

        lo, hi = 0, m
        """
        [lo... i... half ...hi]
        """
        while lo <= hi:
            i = (lo + hi) // 2          # take i elements from nums1 as the left part
            j = half - i                # take j elements from nums2 as the left part

            L1 = nums1[i - 1] if i > 0 else float('-inf')
            R1 = nums1[i]     if i < m else float('inf')
            L2 = nums2[j - 1] if j > 0 else float('-inf')
            R2 = nums2[j]     if j < n else float('inf')

            if L1 > R2:
                # i is too large; move the cut left in nums1.
                hi = i - 1
            elif L2 > R1:
                # i is too small; move the cut right in nums1.
                lo = i + 1
            else:
                # Found a valid partition.
                left_max  = max(L1, L2)
                if (m + n) % 2 == 1:
                    return float(left_max)
                right_min = min(R1, R2)
                return (left_max + right_min) / 2.0


if __name__ == '__main__':
    cases = [
        ([1, 3],     [2],         2.0),
        ([1, 2],     [3, 4],      2.5),
        ([],         [1],         1.0),
        ([2],        [],          2.0),
        ([0, 0],     [0, 0],      0.0),
        ([1],        [2, 3, 4],   2.5),
        ([1, 2, 3],  [4, 5, 6],   3.5),
        ([1, 3, 5, 7], [2, 4, 6, 8], 4.5),
        ([0, 2, 3, 5, 6, 7, 8], [1, 4, 9], 4.5),
        ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5.5),
        ([6, 7, 8, 9, 10], [1, 2, 3, 4, 5], 5.5),
        ([1, 5, 9], [2, 3, 4, 6, 7, 8, 10], 5.5),
    ]
    s = Solution()
    for a, b, expected in cases:
        got = s.findMedianSortedArrays(a, b)
        ok = got is not None and abs(got - expected) < 1e-9
        print(f"{'OK' if ok else 'FAIL'}  nums1={a}, nums2={b}  got={got}, expected={expected}")