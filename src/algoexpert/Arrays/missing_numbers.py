"""
Missing Numbers

You're given an array containing n - 2 distinct positive integers, which
should originally contain all the integers from 1 to n (n being the length
of the array plus 2), but two numbers are missing.

Write a function that returns the two missing numbers in any order.
"""

def missingNumbers(nums):
    # Write your code here.
    """
    Solution(Time: O(n), Space: O(1)) 
    1. The sum of the n numbers should be n * (n + 1) / 2.
    2. The array sum is sum (nums)
    3. The gap between the 2 is the sum of the missing two numbers.
    4. Use the full first half of the numbers substract the sum of the first half numbers in the nums to get the first missing number
    5. Do the same for the second missing number
    6. Return the first and second missiing numbrers in an array 
    """

    total = sum([n for n in range(1, len(nums)+3)])

    missing_sum = total - sum(nums)

    mid = missing_sum // 2

    sum_of_first_half_missing_nums = 0
    sum_of_second_half_missing_nums = 0
    
    for i, n in enumerate(nums):
        if n <= mid:
            sum_of_first_half_missing_nums += n
        else:
            sum_of_second_half_missing_nums += n

    first_total = 0
    second_total = 0
    for j in range(1, len(nums) + 3):
        if j <= mid:
           first_total += j
        else:
            second_total +=j

    return [first_total - sum_of_first_half_missing_nums, second_total - sum_of_second_half_missing_nums]
    