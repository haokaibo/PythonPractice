"""
Reverse Words in a String II (In-Place, Character Array Version)

Follow-up to LeetCode 151: instead of a string, you're given an array of
characters representing a string. Reverse the order of the words in-place.

A word is defined as a sequence of non-space characters.

Do not allocate another array of strings: you must do this in-place with
O(1) extra space.

Example:
Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
"""

"""
1. Iterate the s array in reverese order, and reverse the whole string from the end to begin
2. Reverse the words in the string
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s.reverse()
        j = 0
        while j < len(s):
            begin = j
            while j < len(s) and s[j] != ' ':
                j += 1
            end = j - 1
            while begin < end:
                s[begin], s[end] = s[end], s[begin]
                begin += 1
                end -= 1
            j = j + 1
        return s
                
if __name__ == "__main__":
    print(Solution().reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))