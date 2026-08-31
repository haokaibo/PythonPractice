"""
Solution:
1. use count sort to do the in place sorting in the target array
Time: O(n+k), O(k). k is the size of the colors
"""
class Solution(object):
    def sort_colors_dutch_flag(self, arr):
        low = mid = 0
        high = len(arr) - 1
        print(f'arr={nums}, low={low}, mid={mid}, high={high}')
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
            
            print(f'arr={nums}, low={low}, mid={mid}, high={high}')
       
        return arr
        
    def countSort(self, nums):
        colors = [0, 0, 0]
        for num in nums:
            colors[num] +=1
        
        index = 0
        for color, count in enumerate(colors):
            for _ in range(count):
                nums[index] = color
                index += 1

        return nums
        
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        return self.sort_colors_dutch_flag(nums)
        

if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]

    print(nums)
    Solution().sortColors(nums)
    print(nums)
