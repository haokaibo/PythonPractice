"""
Max Subset Sum No Adjacent

You're given an array of positive integers. Write a function that calculates
the maximum sum of non-adjacent elements in the array.

For example, given an array [3, 7, 4, 6, 5], the maximum sum of
non-adjacent elements is 13 (7 + 6).
"""

"""
Solution(Time: O(nLog(n), Space: O(1))
Use the first variable to hold the max sum we got for the previous iteration.
Use the second variable to hold the max sum we got for the iteration before the previous one.
For each number in the array, we have two options:
1. Include the number: In this case, we add the number to the max sum from two iterations ago.
2. Exclude the number: In this case, we just take the max sum from the previous iteration.
We take the maximum of these two options as the new max sum for the current iteration.
"""
def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if not array:
        return 0
    elif len(array) == 1:
        return array[0]
    
    second = array[0]
    first = max(array[0], array[1])

    for n in array[2:]:
        current = max(first , second + n)
        second = first
        first = current
    
    return first

print(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]))