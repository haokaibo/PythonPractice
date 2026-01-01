
def firstNonRepeatingCharacter(string):
    # Write your code here.
    """
    Solution(Time: O(n), Space: O(c), c is the unique characters in the string)
    Build a dict to hold the unique characters in the string.
    Iterate the string, if a single character is not in the dict, add it to the dict and set the value to index of the item in the string. 
    Iterate the dict and return the first count is non negative char
    """ 
    unique_chars = dict()

    if string is None or len(string) == 0:
        return -1

    for i in range(len(string)):
        if string[i] not in unique_chars:
            unique_chars[string[i]] = i
        else:
            unique_chars[string[i]] = -1            

    for k, v in unique_chars.items():
        if v >= 0:
            return v

    return -1