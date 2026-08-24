"""
Product Sum

Write a function that takes in a "special" array and returns its product sum.

A "special" array is defined as an array that contains either integers or
other "special" arrays.

The product sum of a "special" array is the sum of its elements, where each
element in the array is multiplied by a depth factor. At the top-level, the
depth factor is 1. The depth factor of a subarray's elements is equal to the
subarray's depth + 1. For instance, the array [1, 2, [3, 4], 5] is a
"special" array of depth 1. It contains a subarray in the form of [3, 4],
whose product sum is (3 * 2) + (4 * 2). Therefore, the product sum of
[1, 2, [3, 4], 5] is 1 + 2 + (3 * 2) + (4 * 2) + 5 = 21.
"""

# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.

def product_sum(array, depth=1):
    total = 0
    for item in array:
        if type(item) == int:
            total += item
        elif type(item) == list:
            total += (depth + 1) * product_sum(item, depth + 1)
    return total

    # [5, 2, [7, -1]]]
    # total = 5
    # total = 7
    # total = 7 + 2 * product_sum([7, -1], 2) = 7 + 2 * 6 = 21

def productSum(array):
    # Write your code here.
    # Solution
    # The depth of the "special" array is incremented for each layer
    # use variable depth to ensure the calculation
    # The formula is sum (elements in arrays) * depth
    # This is a recursive calculation
    # Time complexity: O(n)
    # Space complexity: O(d) - d is the deepest depth of the special arrays
    return product_sum(array)