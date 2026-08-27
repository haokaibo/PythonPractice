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
Solution (Trie + DFS):
1. Build a Trie from all words. Each node stores its children and the full word at the terminal node.
2. For each cell on the board, if the char exists in Trie root's children, start DFS from there.
3. DFS explores 4 directions (up, down, left, right), following the Trie path.
4. Mark visited in-place by setting board[r][c] = '#' (saves extra space).
5. When a Trie node has a word, add to result and set word=None to avoid duplicates.
6. Pruning: if a Trie node's children become empty after DFS, remove it from its parent
   (dead-end pruning, prevents redundant exploration in subsequent DFS calls).

Time: O(m * n * 3^L) where m*n = board size, L = max word length
Space: O(m * n) recursion stack depth + O(T) for Trie, T = total chars across all words
"""

class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = None  # 在单词结尾节点直接存储完整单词，避免手动拼字符串


class Solution(object):

    def findWords(self, board, words):
        # 1. 构建前缀树 (Trie)
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        res = []
        rows, cols = len(board), len(board[0])

        # 2. DFS 探索函数
        def dfs(r, c, parent):
            char = board[r][c]
            curr_node = parent.children[char]

            # 找到匹配单词
            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None  # 避免重复匹配相同的单词

            # 标记已访问（直接修改原矩阵节省 space/time）
            board[r][c] = "#"

            # 3. 向上下左右四个方向探索
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and board[nr][nc] in curr_node.children
                ):
                    dfs(nr, nc, curr_node)

            # 回溯：恢复原始字符
            board[r][c] = char

            # 剪枝优化（防止多余计算）
            if not curr_node.children:
                parent.children.pop(char)

        # 3. 遍历网格起点，只需检查在 Trie 根节点下的字符
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return res
