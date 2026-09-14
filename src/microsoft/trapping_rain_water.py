"""
# 题目 (LeetCode 42. 接雨水 / Trapping Rain Water)
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，
# 下雨之后能接多少雨水。
#
# 示例 1：
#   输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
#   输出：6
#   解释：可以接 6 个单位的雨水
#
# 示例 2：
#   输入：height = [4,2,0,3,2,5]
#   输出：9
#
# 提示：
#   n == height.length
#   1 <= n <= 2 * 10^4
#   0 <= height[i] <= 10^5
#
# 难度：困难
#
# 解题思路：双指针法
#   左右两个指针从两端向中间移动，left_max 和 right_max 分别记录两侧最大值。
#   每次移动较矮的一侧：
#     - 若当前柱高 >= 该侧最大值，则更新最大值（此柱无法蓄水）
#     - 否则累加 (该侧最大值 - 当前柱高) 到总水量
#   因为较矮一侧的蓄水上限由它自身的最大值决定（另一侧必有更高的柱子兜底）。
#
# 复杂度：
#   时间复杂度：O(n)，单次遍历
#   空间复杂度：O(1)，仅用常数额外空间
"""

class Solution(object):

  def trap(self, height):
    if not height:
      return 0

    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    total = 0

    while left < right:
      if height[left] < height[right]:
        if height[left] >= left_max:
          left_max = height[left]
        else:
          total += left_max - height[left]
        left += 1
      else:
        if height[right] >= right_max:
          right_max = height[right]
        else:
          total += right_max - height[right]
        right -= 1

    return total