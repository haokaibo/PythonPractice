"""
LeetCode 151. Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in the
input string will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single
space.

Note that s may contain leading or trailing spaces or multiple spaces
between two words. The returned string should only have a single space
separating the words and do not contain any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello   world  "
Output: "world hello"
Explanation: Your reversed string must not contain leading or trailing
spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a
single space in the reversed string.
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        e.g. "the sky is blue"
        " "
        """
        words = []
        i = len(s) - 1
        while i > -1:
            # look for none space character
            while  i > -1 and s[i] == ' ':
                i -= 1
            if i < 0:
                break
                
            end = i
            i = i - 1
            
            while i > -1 and s[i] != ' ':
                i -= 1
            
            begin = i + 1
            
            words.append(s[begin:end+1])
            
        return ' '.join(words)

if __name__ == "__main__":
    print(Solution().reverseWords("the sky is blue"))