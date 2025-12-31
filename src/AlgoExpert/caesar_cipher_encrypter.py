def caesarCipherEncryptor(string, key):
    # Write your code here.
    # Solution 
    # Iterate the string characters, get the ascii code for each character by ord() function, 
    # n , n + 1, ... , n + 26
    # char(( ord(n) - ord('a') + k ) % 26 + ord('a'))
    # use chr() function to convert the ascii code to a character
    # Time complexity is O(n)
    # space complexity is O(n)
    encrypted = []
    
    for c in string:
        encrypted.append(chr((ord(c) - ord('a') + key) % 26 + ord('a')))

    return ''.join(encrypted)
