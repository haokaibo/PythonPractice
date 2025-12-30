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