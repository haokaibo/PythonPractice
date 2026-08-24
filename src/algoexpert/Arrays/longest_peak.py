"""
Longest Peak

You're given an array of integers where the integers are in an arbitrary
order. Write a function that returns the length of the longest peak in the
array.

A peak is defined as a sequence of adjacent ints in the array that strictly
increment until they reach a tip and then strictly decrement. The length of
a peak is the difference between its last index and its first index + 1. For
a sequence of one or two integers, it's impossible to have a peak sequence,
so the length of the longest peak would be 0.

Note that a peak won't be possible at the first or last index.
"""

def longestPeak(array):
    # Write your code here.
    """
    Solution(Time: O(n), space: O(1))
    Peak judgement: Strictly increasing and decreasing
    """
    longest_peak = 0
    # 1 2 3 4 0
    # 1 2
    # 1 2 2 0
    # 2 1
    for i in range(1, len(array)):
        peak = 0
        while i < len(array) and array[i] > array[i-1]:
            i += 1
            peak += 1

        # not peak (1. No further element, 2. No adjacent decreasing element), 3. No previous increasing
        if i == len(array) or array[i] == array[i-1] or peak == 0:
            i += 1
            continue

        
        while i < len(array) and array[i] < array[i-1]:
            i += 1
            peak +=1

        if peak + 1 > longest_peak:
            longest_peak = peak + 1 # The first element of the peak should be included

    return longest_peak
