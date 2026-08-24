"""
Palindrome Check

Write a function that takes in a string and determines whether it's a
palindrome or not.

A palindrome is defined as a string that reads the same forwards and
backwards. The input string might contain special characters, spaces, and
capital letters. In other words, "A man, a plan, a canal: Panama" is a
palindrome. It shouldn't be case-sensitive, and it shouldn't consider
special characters or spaces.
"""

def isPalindrome(string):
    # Write your code here.
    # Solution
    # Iterate the string from the begin and end together. 
    # If all the begin and end are always the same, then it is a palindrome, else it is not.
    # Time complexity: O(n)
    # Space complexity: O(1)
    begin = 0
    end = len(string) - 1

    while begin <= end:
        if string[begin] != string[end]:
            return False
        begin += 1
        end -= 1

    # abc a c False
    # aba a a b b True
    # aa a a True
    return True
