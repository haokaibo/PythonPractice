
"""
Monotonic Array

Write a function that takes in an array of integers and returns a boolean
representing whether the array is monotonic or not.

An array is said to be monotonic if its values don't decrease as you move
through it from left to right, or if its values don't increase as you move
through it from left to right.

Put another way, an array is monotonic if its values only ever increase or
only ever decrease. Note that single-valued arrays are monotonic.
"""

def isMonotonic(array):
    # Write your code here.
    """
    Solution(Time: O(n). Space: O(1))
    Iterate the array to check if array[i] <= array[i + 1] (increasing) or  array[i] >= array[i + 1] (descreasing)

    """

    trend = None
    for i in range(len(array)):
        if i + 1 == len(array):
            break

        if  array[i+1] > array[i]:
            increasing = 1
        elif array[i+1] < array[i]:
            increasing = -1
        else:
            increasing = 0
            
        if trend == None: # first element
            trend = increasing
            continue

        elif increasing == 0:
            # no matter whether the previous trend is increasing, decreasing or flat, this doesn't change any
            continue
        elif trend != increasing:
            if trend == 0:
                trend = increasing
            else:
                return False
            # print(f"array[i], array[i+1]={array[i], array[i+1]}")

    return True

def optimized_isMonotonic(array):
    c = True
    d = True

    for i in range(1, len(array)):
        c = c and array[i] >= array[i-1]
        d = d and array[i] <= array[i-1]

    return c or d
print(isMonotonic([-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -8, -9, -10, -11]))