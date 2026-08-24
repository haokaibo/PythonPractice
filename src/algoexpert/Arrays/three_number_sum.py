"""
Three Number Sum

Write a function that takes in a non-empty array of distinct integers and an
integer representing a target sum. The function should find all triplets in
the array that sum up to the target sum and return a two-dimensional array
of all these triplets. The numbers in each triplet should be ordered in the
order in which they appear in the input array, and the triplets themselves
should be sorted in respect to the first numbers in each triplet.

If no three numbers sum up to the target sum, the function should return an
empty array.
"""

def threeNumberSum(array, targetSum):
    # Write your code here.
    """
    Optimized Solution 2
    Time: O(n^2)
    Space: O(log(n))
    """
    triplets = []
    array.sort()

    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1

        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif current_sum > targetSum:
                right -= 1
            elif current_sum < targetSum:
                left += 1

    return triplets