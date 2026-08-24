def zeroSumSubarray(nums):
    # Write your code here.
    """
    Solution(Time: O(n), Space: O(n))
    1. Use a set to hold the numbers in the list.
    2. Iterate the array, if the iteration number is 0, just ignore.
    3. else use a sum to calculate the cumulative sum.
    4. If the iteration number is not 0, and cumulative sum is in the current set, return true
    """
    if nums is None or len(nums) == 0:
        return False
    uniqueSums = set()
    uniqueSums.add(0)
    cumulativeSum = 0
    for i, n in enumerate(nums):
        cumulativeSum += n
       
        if cumulativeSum in uniqueSums:
            return True
        else:
            uniqueSums.add(cumulativeSum)
        
    
    return False