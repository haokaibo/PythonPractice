"""
Four Number Sum

Write a function that takes in a non-empty array of integers and an integer
representing a target sum. The function should find all quadruplets in the
array that sum up to the target sum and return a two-dimensional array of
all these quadruplets. The numbers in each quadruplet should be ordered in
the order in which they appear in the input array, and the quadruplets
should be sorted in respect to the first numbers in each quadruplet.

For example, given array = [4, 5, 1, -3, 6, 8] and targetSum = 11, the
function should return [[4, 5, 1, 1], [5, 6, -3, 3]]. Note that duplicate
numbers in the same quadruplet are allowed if they appear in the input array.

If no four numbers sum up to the target sum, the function should return an
empty array.
"""

def fourNumberSum(array, targetSum):
    # Write your code here.
    """
    Optimized Solution: Time: O(n^2), Space: O(n^2)
    
    Strategy:
    1. Use a hash map to store all pair sums encountered so far
    2. For each element, find its complement in the hash map to form quadruplets
    3. Store all pair sums ending at current index to avoid duplicate quadruplets
    
    Key insights:
    - Store pair sums by their ending index to maintain order
    - Use dictionary to map pair sums to lists of index pairs
    - Find quadruplets by looking for targetSum - currentPairSum in previous pairs
    """
    allPairSums = {}
    quadruplets = []
    n = len(array)
    
    for i in range(1, n - 1):
        # Find quadruplets that end at current position
        for j in range(i + 1, n):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if difference in allPairSums:
                for pair in allPairSums[difference]:
                    quadruplets.append(pair + [array[i], array[j]])
        
        # Store all pairs that end at current position
        for k in range(0, i):
            pairSum = array[i] + array[k]
            if pairSum not in allPairSums:
                allPairSums[pairSum] = [[array[k], array[i]]]
            else:
                allPairSums[pairSum].append([array[k], array[i]])
                
    return quadruplets


# Example usage and test cases
if __name__ == "__main__":
    # Test case 1: Basic example
    array1 = [4, 5, 1, -3, 6, 8]
    target1 = 11
    result1 = fourNumberSum(array1, target1)
    print(f"Test 1 - Array: {array1}, Target: {target1}")
    print(f"Quadruplets: {result1}")
    print()
    
    # Test case 2: Empty result
    array2 = [1, 2, 3, 4]
    target2 = 100
    result2 = fourNumberSum(array2, target2)
    print(f"Test 2 - Array: {array2}, Target: {target2}")
    print(f"Quadruplets: {result2}")
    print()
    
    # Test case 3: All same numbers
    array3 = [1, 1, 1, 1, 1]
    target3 = 4
    result3 = fourNumberSum(array3, target3)
    print(f"Test 3 - Array: {array3}, Target: {target3}")
    print(f"Quadruplets: {result3}")
    print()
    
    # Test case 4: Negative numbers and positives
    array4 = [-1, -2, -3, 0, 1, 2, 3, 4]
    target4 = 0
    result4 = fourNumberSum(array4, target4)
    print(f"Test 4 - Array: {array4}, Target: {target4}")
    print(f"Quadruplets: {result4}")
    print()
    
    # Test case 5: Larger array
    array5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target5 = 20
    result5 = fourNumberSum(array5, target5)
    print(f"Test 5 - Array: {array5}, Target: {target5}")
    print(f"Quadruplets: {result5}")