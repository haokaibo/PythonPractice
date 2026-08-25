"""
LeetCode 8. String to Integer (atoi)

Implement a function myAtoi(string s) that converts a string to a 32-bit
signed integer.

The algorithm should implement the following steps:

1. Skip leading whitespaces.
   In other words, skip all characters until the first non-whitespace
   character is found. If no non-whitespace characters exist, return 0.

2. Determine the sign.
   If the first non-whitespace character is '-', take the result as
   negative. Otherwise, assume it is positive.

3. Convert digits.
   Starting from the first non-whitespace character, take the largest
   possible prefix of the string consisting only of digits as the integer
   base.

4. Build the integer.
   Let the integer be (sign) * (converted prefix). If the prefix is empty,
   or the only digit is '0', then the integer is 0.

5. Handle overflow.
   The actual value may be out of the 32-bit signed integer range
   [-2^31, 2^31 - 1]. If the integer is out of the range, use the boundary
   value as the final integer: if the integer is greater than 2^31 - 1,
   return 2^31 - 1, and if it is less than -2^31, return -2^31.
"""

"""
use a string array to hold the valid characters

since: s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

classify the input chars into categories

digits: 0-9
for 0 checking the leading char is sign or digit
    sign: ignore
    digit: add to target
space: ' '
signs: '+', '-'
dot: '.'(since the target is an integer, we ignore this char)

Direction: from left to right

"0-9" keep it 
" " ignore it
'+' / '-' if there is len(string array) is empty, add it to the array, else stop iteration
'.' stop iteration

check the range max(-2**31, min(target, 2**31 - 1)) 

"""

"""1337c0d3"""


class Solution(object):
    def is_digit(self, c):
        digits = [str(i) for i in range(10)]
        return c in digits
    
    def is_sign(self, c):
        return c in ['+', '-']
    
    
    def is_space(self, c):
        return c == ' '
    
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        target = []
        sign = ''

        for c in s:
            if self.is_digit(c):
                # check is 0
                target.append(c)

            elif self.is_sign(c):
                # there is already a sign assigned, the second sign stops the iteration
                if self.is_sign(sign): 
                    break
                # there is a digit in the previous position in the target array, stops the iteration
                if len(target) > 0:
                    break
                sign = c
            
            elif self.is_space(c):
                continue
            else: #.abc
                break
        
        target_num = int(sign + "".join(target))
        return max(-2**31, min(target_num, 2**31 -1))