# Time Complexity

# O(N * M) where N is the number of strings and M is the average string length, due to set construction (O(M) per string) and intersection (O(min set sizes)). Optimal for this task.

def commonCharacters_optimized(strings):

    return list(set.intersection(*map(set, strings)))


def commonCharacters(strings):
    # Write your code here.
    # Solution
    # Time complexity: O(n*c) - n is the string array length, c is the character counts
    # Space comlexity: O(c) - c is the size of the first string in the string list.
    # Use a dict to hold the common characters and it appears count for each string array
    chars = dict()

    for c in strings[0]:
        chars[c] = 1
        
    for i in range(1, len(strings)):
        for c in strings[i]:
    # Check the dict items, if the value of the item is equals to the strings arrays length then it is the common character
            if c in chars:
                chars[c] = i + 1

        # keep the common chars only in the dict.
        chars = {k: v for k, v in chars.items() if v == i + 1}
        
    # Then just output those matched strings in an array
    
    return [c for c in chars]
