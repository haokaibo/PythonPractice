# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

"""
Solution:
1. The celebrity shoud be the one in the pattern [0, 0, ..., 1, 0, 0, 0]
2. The other should be the one in pattern [1, 1, 0, 0, 1, 0, 0, 0, 0]
3. Time complexity should be less than O(3*n)
4. The size of the matrix is n * n
[
    [1 1 0]
    [0 1 0]
    [1 1 1]
]
5. use two rounds of the identity checking of the celebrity. 
    5.1 The first round check the possible one who is known to others and knows no one.
    5.2 The second round check if the chosen one is known to others and doesn't know the others.
     
Time: O(3n-3), Space: O(1)
"""
def knows(i, j):
    pass

class Solution(object):
    
    
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        # find someone who others knows him, but he know no one
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
                
        for i in range(n):
            if i != candidate:
                if knows(candidate, i) or not knows(i, candidate):
                    return -1
                
        return candidate
                
        
        
        