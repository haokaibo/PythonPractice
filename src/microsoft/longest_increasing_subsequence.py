"""

question: why is the result is 4(2, 3, 7, 101)? there is a 5 between 2 and 3, from 5 to 3 is descreasing.
The result should be 3(3, 7, 101)

The way to count the longest subsequence
1. Iterate the array
2. Use a param - count to hold the count of items of the strictly increasing subsequence.
3. The breaking condition: the current - previous < 0 -> reset the count
4. Use a param maxLen to hold the max length can get from the iteration
Time: O(n), Space: O(1)
e.g. 
[2, 3, 4]
[1, 2, 1, 2, 3]
[1, 2, 1, 3, 5] - > [1, 3, 5]
[1, 20, 11, 33, 21, 23, 25, 27]
{(2, 2), (1, 1), (3, 1)}


"""
import bisect

class Solution(object):
    """
    Time: O(n^2), Space: O(n)
    """
    def naiveSolution(self, nums):
        if not nums:
            return 0
        
        sequences =[] # hold the k:v = max item in the sub sequence: len of the sequence
        previous = float('-inf')
        count = 0
        
        """
        [10,9,2,5,3,7,101,18]
        """
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                
        return max(dp)

    """
    Time: O(nlog(n)), Space: O(n)
    """
    def dyanmicPlanning(self, nums):
        tails = []
        for num in nums:
            # 手写二分查找 (bisect_left 的等价实现)
            left, right = 0, len(tails)
            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid
        
            # 如果 num 比 tails 里所有数都大，直接追加
            if left == len(tails):
                tails.append(num)
            # 否则替换掉第一个大于等于 num 的数
            else:
                tails[left] = num
                    
            return len(tails)

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.dyanmicPlanning(nums)
                
        
                
        
            
        