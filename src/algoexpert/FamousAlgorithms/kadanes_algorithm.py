"""
Kadane's Algorithm

Given an array of integers, find the maximum sum of a contiguous subarray.

For example, given the array [3, -1, 2, 1, -3, 4, -1, 2, 1, -5, 4], the maximum
subarray sum is 6 (from subarray [2, 1, -3, 4, -1, 2, 1]).

Key Insights:
- Use Kadane's algorithm: for each element, decide whether to include it in the
current subarray or start a new subarray from this element.
- Track both the maximum sum ending at the current position and the overall
maximum sum found so far.
- Handle edge cases like empty arrays.
"""

def kadanesAlgorithm(array):
    """
    Return the maximum sum of any contiguous subarray.
    
    Time complexity: O(n) - single pass through the array
    Space complexity: O(1) - only constant extra space used
    """
    if not array:
        return None
    
    # max_ending_here represents the maximum sum of subarray ending at current position
    max_ending_here = array[0]
    # max_so_far represents the maximum sum of any subarray found so far
    max_so_far = array[0]
    
    for num in array[1:]:
        # Decide whether to include current number in the subarray or start a new one
        max_ending_here = max(num, max_ending_here + num)
        # Update the overall maximum sum found so far
        max_so_far = max(max_so_far, max_ending_here)
        
    return max_so_far


# Example usage and test cases
if __name__ == "__main__":
    # Test case 1: Basic example
    test_array1 = [3, -1, 2, 1, -3, 4, -1, 2, 1, -5, 4]
    result1 = kadanesAlgorithm(test_array1)
    print(f"Test 1 - Array: {test_array1}")
    print(f"Maximum subarray sum: {result1}")
    print()
    
    # Test case 2: All negative numbers
    test_array2 = [-2, -3, -1, -5]
    result2 = kadanesAlgorithm(test_array2)
    print(f"Test 2 - Array: {test_array2}")
    print(f"Maximum subarray sum: {result2}")
    print()
    
    # Test case 3: All positive numbers
    test_array3 = [1, 2, 3, 4, 5]
    result3 = kadanesAlgorithm(test_array3)
    print(f"Test 3 - Array: {test_array3}")
    print(f"Maximum subarray sum: {result3}")
    print()
    
    # Test case 4: Empty array
    test_array4 = []
    result4 = kadanesAlgorithm(test_array4)
    print(f"Test 4 - Array: {test_array4}")
    print(f"Maximum subarray sum: {result4}")
    print()
    
    # Test case 5: Single element
    test_array5 = [7]
    result5 = kadanesAlgorithm(test_array5)
    print(f"Test 5 - Array: {test_array5}")
    print(f"Maximum subarray sum: {result5}")
    print()
    
    # Test case 6: Array with single positive at start
    test_array6 = [10, -5, -2, 7, -10]
    result6 = kadanesAlgorithm(test_array6)
    print(f"Test 6 - Array: {test_array6}")
    print(f"Maximum subarray sum: {result6}")