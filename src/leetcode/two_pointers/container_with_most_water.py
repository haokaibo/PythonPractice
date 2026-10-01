"""
Container With Most Water

You are given an integer array height of length n.

There are n vertical lines drawn such that the two endpoints of the
ith line are (i, 0) and (i, height[i]).

Find two lines that, together with the x-axis, form a container such
that the container contains the most water.

Return the maximum amount of water the container can store.

Notice that you cannot slant the container.

Example 1:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The vertical lines are represented by the array
    [1,8,6,2,5,4,8,3,7]. In this case, the maximum area of water the
    container can store is 49. The container uses the lines at index 1
    (height 8) and index 8 (height 7), giving min(8,7) * (8-1) = 49.

Example 2:
    Input: height = [1,1]
    Output: 1

Constraints:
    - 2 <= n <= 10^5
    - 0 <= height[i] <= 10^4
"""

from typing import List


def maxArea(height: List[int]) -> int:
    """
    Optimized Solution: Time: O(n), Space: O(1)

    Strategy:
    1. Use two pointers — one at the start (left) and one at the end (right).
    2. The container width is (right - left) and the height is
       min(height[left], height[right]).
    3. Compute the area and track the maximum.
    4. Move the pointer pointing to the shorter line inward, because the
       shorter line is the limiting factor; keeping it while shrinking the
       width can never yield a larger area, so discarding the shorter line
       is safe (it cannot participate in any better solution).

    Key insight:
    - Area = min(h[left], h[right]) * (right - left).
    - Always advance the shorter of the two lines to search for a taller
      line that could compensate for the reduced width.

    Time complexity  : O(n) — each element is visited at most once.
    Space complexity : O(1) — only a few integer variables are used.
    """
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        # Compute the current container area
        width = right - left
        current_height = min(height[left], height[right])
        current_area = current_height * width
        max_area = max(max_area, current_area)

        # Move the shorter line inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


# Example usage and test cases
if __name__ == "__main__":
    # Test case 1: LeetCode example
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 6]
    result1 = maxArea(height1)
    print(f"Test 1 - Height: {height1}")
    print(f"Max area: {result1} (expected: 49)")
    print()

    # Test case 2: Two equal lines
    height2 = [1, 1]
    result2 = maxArea(height2)
    print(f"Test 2 - Height: {height2}")
    print(f"Max area: {result2} (expected: 1)")
    print()

    # Test case 3: Ascending heights
    height3 = [1, 2, 3, 4, 5]
    result3 = maxArea(height3)
    print(f"Test 3 - Height: {height3}")
    print(f"Max area: {result3} (expected: 6)")
    print()

    # Test case 4: Descending heights
    height4 = [5, 4, 3, 2, 1]
    result4 = maxArea(height4)
    print(f"Test 4 - Height: {height4}")
    print(f"Max area: {result4} (expected: 6)")
    print()

    # Test case 5: Tallest lines in the middle
    height5 = [2, 3, 10, 5, 7, 8]
    result5 = maxArea(height5)
    print(f"Test 5 - Height: {height5}")
    print(f"Max area: {result5} (expected: 24)")


    # Test case 6: LeetCode canonical example
    height6 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result6 = maxArea(height6)
    print(f"Test 6 - Height: {height6}")
    print(f"Max area: {result6} (expected: 49)")
