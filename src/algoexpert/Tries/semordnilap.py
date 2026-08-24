# O(n * m) time | O(n * m) space, n the word count in the string list. m is the max chars in a word.
def semordnilap(words) :
    wordsSet = set(words)
    semordnilapPairs =［］
    for word in words:
        reverse = word [::-1]
        if reverse in wordsSet and reverse != word: 
            semordnilapPairs.append([word, reverse])
            wordsSet.remove(word)
            wordsSet.remove (reverse)
return semordnilapPairs