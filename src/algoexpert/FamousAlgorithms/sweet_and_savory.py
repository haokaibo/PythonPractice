"""
Sweet And Savory

You're given an array of dishes, where each dish is represented by a single
integer: a negative integer represents a sweet dish whose sweetness is the
absolute value of the integer, and a positive integer represents a savory
dish whose savoriness is the integer itself.

Write a function that returns the pair of dishes (one sweet and one savory)
whose combined taste is as close as possible to a given target value without
exceeding it. If no valid pair exists, the function should return [0, 0].
"""

import math
def sweetAndSavory(dishes, target):
    # Write your code here.
    """
    Solution(Time: O(nlog(n)), Space: O(n))
    Sort the array and split the array into negative(Sweet) and positive(savory) ones.
    Calculate the sum of the two array elements by iteration, if the sum is smaller than
    the target, move the index of the savory array to later items. else move the index
    in the sweet array
    """
    bestPair = [0, 0]
    sweets = sorted([d for d in dishes if d < 0], key=abs)
    savorys = sorted([d for d in dishes if d > 0])

    sweetIndex = 0
    savoryIndex = 0

    bestGap = float("inf")

    while sweetIndex < len(sweets) and savoryIndex < len(savorys):
        currentSum = sweets[sweetIndex] + savorys[savoryIndex]

        if currentSum <= target:
            currentGap = target - currentSum
            if currentGap <= bestGap:
                bestGap = currentGap
                bestPair = [sweets[sweetIndex], savorys[savoryIndex]]
            savoryIndex +=1
        else:
            sweetIndex += 1

    
    return bestPair