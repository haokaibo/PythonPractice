def moveElementToEnd(array, toMove):
    # Write your code here.
    """
    Solution(Time: O(n), space: O(1))
    1. Iterate the array from the left and the right together
    2. If the left item equals the toMove, find the right non-toMove element, then swap
    """
    left = 0
    right = len(array) - 1

    while left < right:
        if array[left] == toMove:
            while left < right and array[right] == toMove:
                right -= 1
            array[left], array[right] = array[right], array[left]
            right -= 1
        left += 1

    return array    

