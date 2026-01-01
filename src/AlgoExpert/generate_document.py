def generateDocument(characters, document):
    # Write your code here.
    # Solution
    # Time complexity: O(m + n) : m is the length of hte characters, n is the length of the document
    # Space complexity: O(c) : c is the unique characters in the characters.
    # 1. convert the char in characters into a dict. The key is the unique char, the value is the appearance of the unique char in the characters.
    chars = dict()
    for c in characters:
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1
    # 2. Iterate the document, if a single char in the document cannot be found in the char dict or the char value is less than 1 then return False.
    for d in document:
        if d not in chars or chars[d] == 0:
            return False
        
    # 3. Else the count of the char value should substract 1.
        else:
            chars[d] -= 1
    
    return True
