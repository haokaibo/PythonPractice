"""
LeetCode 17. Letter Combinations of a Phone Number [Medium]

Given a string containing digits from 2-9 only, return all possible letter
combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on a telephone keypad) is given below:

    2: abc    3: def    4: ghi
    5: jkl    6: mno    7: pqrs
    8: tuv    9: wxyz

Note: 1 has no letters mapped to it.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9']
"""

"""
Solution (Iterative):
There are m * n combinations for number keys combinations, m, n are the char count of each keys.
1. Build a num dict with num: chars dict
2. Iterate the digits to build the combinations
3. Use a for loop to iterate all the combinations

Time: O(3^m * 4^n) where m = count of digits with 3 letters, n = count of digits with 4 letters
Space: O(3^m * 4^n) for the result
"""
class Solution(object):
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        nums = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        combinations = []
        
        for d in digits:
            if d in nums:
                if len(combinations) == 0:
                    combinations = [c for c in nums[d]]
                else:
                    combinations = [x + y for x in combinations for y in nums[d]]        
                
        
        return combinations
        
        