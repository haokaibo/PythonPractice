"""
Semordnilap

You're given an array of words where each word can contain only English
lowercase alphabetic characters. Write a function that returns all
semordnilap pairs from this array.

A semordnilap pair is a pair of words that become each other when reversed.
For example, "diaper" and "repaid" is a semordnilap pair. Note that
palindromes (words that are the same when reversed) are not semordnilap
pairs.

The words in each semordnilap pair you return should both appear in the
input array in their original form.
"""

# O(n * m) time | O(n * m) space, n the word count in the string list. m is the max chars in a word.
def semordnilap(words) :
    wordsSet = set(words)
    semordnilapPairs = []
    for word in words:
        reverse = word [::-1]
        if reverse in wordsSet and reverse != word: 
            semordnilapPairs.append([word, reverse])
            wordsSet.remove(word)
            wordsSet.remove (reverse)
    return semordnilapPairs