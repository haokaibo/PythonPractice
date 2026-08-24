"""
Run Length Encoding

You're given a non-empty string that contains only alphanumeric characters
(characters between 0-9 and a-z). The characters in the string are arranged
in runs where each run consists of a character repeated one or more times.
For example, the characters "x", "x", and "d" in the string "xxdd" form a
run of "x" and a run of "d". Write a function that returns the run-length
encoded string.

For example, the string "xxddd" would be run-length encoded as "x2d3".

This function should return the run-length encoded string only if it's
shorter than the original string. If it doesn't make the string shorter, the
function should return the original input instead. If a run of length 10 or
more occurs in the input string, the string should never be run-length
encoded.
"""

def runLengthEncoding(string):
    # Write your code here.
    # Solution
    # Time complexity: O(n)
    # Space complexity: O(n)
    # Create an array to hold compressed characters.
    array = []
    counter = 1
    # Iterate the string object, use a variable to hold the previous character
    # A
    # if len(string) == 1:
    #     return f"1{string}"

    # AAB -> 2AB
    for i in range(1, len(string)):
        
        if string[i-1] != string[i] or counter == 9:                
            array.append(f"{counter}{string[i-1]}")
            counter = 1
        else:
            counter += 1

    # Handle the last character
    array.append(f"{counter}{string[len(string)-1]}")
    # join the elements in the array to a string as the return
    return "".join(array)
