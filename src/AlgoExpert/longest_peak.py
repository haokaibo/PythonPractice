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
