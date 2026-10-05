"""
Largest Range

Write a function that takes in an array of integers and returns an array
of length 2 representing the largest range of numbers contained in the
array.

A "range" is a set of consecutive integers with no gaps (e.g. [0, 1, 2, 3,
4] is a range of length 5). The numbers in the range do NOT need to appear
consecutively in the input array. A single number is considered a range of
length 1.

The returned array should contain the two endpoints of the range, in order
from smallest to largest. If there is a tie, any valid largest range may be
returned.

Sample Input:
    array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]

Sample Output:
    [0, 7]
    # The range [0, 7] covers {0, 1, 2, 3, 4, 5, 6, 7} which is the
    # longest sequence of consecutive integers found in the array.

Time Complexity: O(n) — each number is visited at most twice (once in the
outer loop and once during range expansion).
Space Complexity: O(n) — the hash table storing all numbers.
"""
def largestRange(array):
    numbers = {num: True for num in array}
    bestRange = []
    longestLength = 0
    
    for num in array:
        # 如果当前数字已经被访问过，直接跳过
        if not numbers[num]:
            continue
            
        numbers[num] = False
        currentLength = 1
        left = num - 1
        right = num + 1
        
        # 向左扩展查找连续整数
        while left in numbers:
            numbers[left] = False
            currentLength += 1
            left -= 1
            
        # 向右扩展查找连续整数
        while right in numbers:
            numbers[right] = False
            currentLength += 1
            right += 1
            
        # 更新最大区间
        if currentLength > longestLength:
            longestLength = currentLength
            bestRange = [left + 1, right - 1]
            
    return bestRange