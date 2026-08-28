# first define the Trie class to hold each char in a word

class Trie(object):
    def __init__(self) -> None:
        self.children = {}
        self.word = None

class Solution(object):
    def findWords(self, board, words):
        # build the word Tires
        root = Trie()
        for word in words:
            current = root
            for char in word:
                if char not in current.children:
                    current.children[char] = Trie()
                current = current.children[char]
            current.word = word
        
        res = []
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, parent):
            
            char = board[r][c]
            current = parent.children[char]

            if current.word:
                res.append(current.word)
                current.word = None

            board[r][c] = '#'

            for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (0<=nr<rows and 0<=nc<cols and board[nr][nc] in current.children):
                    dfs(nr, nc, current)

            board[r][c] = char

            if not current.children:
                parent.children.pop(char)
            
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)
        return res

if __name__ == "__main__":
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    print(Solution().findWords(board, words))