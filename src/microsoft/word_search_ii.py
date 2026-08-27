"""
LeetCode 212. Word Search II [Hard]

Given an m x n board of characters and a list of strings words, return all
words on the board. Each word must be constructed from letters of sequentially
adjacent cells, where "adjacent" cells are those horizontally or vertically
neighboring. The same letter cell may not be used more than once in a word.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
       words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a"], ["b"]], words = ["ab"]
Output: ["ab"]

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 12
- board[i][j] and words[k] are consists of lowercase English letters.
- 1 <= words.length <= 3 * 10^4
- 1 <= words[k].length <= 10
- All the values of words are unique.
"""

"""
Solution:
1. Build a dict to hold the chars in the board. e.g. {'a': [(r, c)]}. r is the row, c is the column.
2. For each word, find all starting positions that match the first character.
3. For each starting position, use DFS to traverse 4 directions (up, down, left, right).
4. Stop conditions:
    a. The char in board cannot be matched with the one in the words.
    b. The position is already visited (out of bound or used).
    c. The full word is found (p + 1 == len(word)).

Time: O(W * m * n * 3^L) where W = number of words, m*n = board size, L = max word length
Space: O(m * n) for the visited set per word search
"""

class Solution(object):
    def bfs(self, board, visited, r, c, word, p):
        
        if (r, c) in visited:
            return False
        if p + 1 == len(word):
            return True
        
        char = word[p]
        if board[r][c] == char:
            visited.add((r, c))


            if c + 1 < len(board[0]):
                found = self.bfs(board, visited, r, c + 1, word, p + 1)
                if found:
                    return True
            if c - 1 >= 0:
                found = self.bfs(board, visited, r, c - 1, word, p + 1)
                if found:
                    return True
            if r - 1 >= 0:
                found = self.bfs(board, visited, r - 1, c, word, p + 1)
                if found:
                    return True
            if r + 1 < len(board):
                found = self.bfs(board, visited, r + 1, c, word, p + 1)
                if found:
                    return True
        
        return False
            

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # build the dict
        rows = len(board)
        cols = len(board[0])
        c_dict = dict()
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] not in c_dict:
                    c_dict[board[r][c]] = []
                c_dict[board[r][c]].append((r,c))

        # find the words in board
        matched = []
        
        for word in words:
            char = word[0]
            if char not in c_dict:
                continue

            for n in c_dict[char]:
                r = n[0]
                c = n[1]
                visited = set()
                if self.bfs(board, visited, r, c, word, 0):
                    matched.append(word)
                    break
            
                            
        return matched
                        
                    
        
if __name__ == "__main__":
    found_words = Solution().findWords([["a","a"]], ["aaa"])

    print(found_words)
    
