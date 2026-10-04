# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
"""
Suffix Trie Construction

Write a SuffixTrie class that:
    - Accepts a string and builds a suffix trie from it.
    - Has a contains method that checks whether a string is a substring of
      the original string (i.e. whether it is contained in the suffix trie).

A suffix trie is a trie that contains all the suffixes of a string.
Each suffix should end with the end symbol "*" (a key in the trie node
mapping to True). A suffix trie only stores suffixes; it does NOT store
every substring — the suffixes' prefixes naturally form every substring.

The contains method should return True if the input string is a substring
of the original string (equivalently, a prefix of some suffix stored in
the trie), and False otherwise.

Sample Input/Output:
    # The trie is constructed from the string "abcd"
    trie = SuffixTrie("abcd")
    trie.contains("abc")  # True
    trie.contains("bcd")  # True
    trie.contains("b")    # True
    trie.contains("bd")   # False  (not a contiguous substring)

Intuition:
Iterate the input string char by char.
For each char check if the char is in current node keys,
if not return False
if yes, iterate the values as new keys for the next char of the string.
Time: populateSuffixTrieFrom O(n^2), contains O(M), Space: O(n^2)
"""
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        # Write your code here.
        n = len(string)

        for i in range(n):
            node = self.root
            for j in range(i, n):
                c = string[j]
                if c not in node:
                    node[c] = {}
                node = node[c]

            node[self.endSymbol] = True
            

    def contains(self, string):
        # Write your code here.
        root = self.root
        for c in string:
            if c not in root:
                return False
            root = root[c]

        return self.endSymbol in root
