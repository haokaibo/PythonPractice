def isPalindrome(string):
    # Write your code here.
    # Solution
    # Iterate the string from the begin and end together. 
    # If all the begin and end are always the same, then it is a palindrome, else it is not.
    # Time complexity: O(n)
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
