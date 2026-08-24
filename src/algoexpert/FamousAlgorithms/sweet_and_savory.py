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