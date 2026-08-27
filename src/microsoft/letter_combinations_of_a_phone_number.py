"""
LeetCode 17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 only, return all possible letter
combinations that the number could represent based on how they are mapped on
a telephone keypad. In case a digit maps to more than two letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]
"""

"""
Solution: Backtracking
1. Map each digit to its corresponding letters (2->abc, 3->def, ..., 7/9->pqrs/wxyz)
2. Use DFS/backtracking to build combinations character by character
3. At each step, try every letter for the current digit, then recurse to the next digit
4. Base case: when the current combination length equals digits length, add to result

Time: O(3^m * 4^n) where m = number of digits with 3 letters, n = number of digits with 4 letters
Space: O(3^m * 4^n) for the result; O(len(digits)) for the recursion stack depth
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        result = []
        
        def backtrack(index, path):
            if index == len(digits):
                result.append(path)
                return
            
            for letter in phone[digits[index]]:
                backtrack(index + 1, path + letter)
        
        backtrack(0, "")
        return result


if __name__ == "__main__":
    print(Solution().letterCombinations("23"))
    # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(Solution().letterCombinations("2"))
    # Output: ["a","b","c"]
    print(Solution().letterCombinations(""))
    # Output: []
