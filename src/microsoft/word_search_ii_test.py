"""
Word Search II (力扣 212 题)
============================

问题描述
--------
给定一个 m x n 二维字符网格 board 和一个单词列表 words，
找出所有同时在网格和单词列表中存在的单词。

单词必须按照字母顺序，通过相邻（上下左右）单元格内的字母构成。
同一个单元格内的字母在一个单词中不允许重复使用。

示例
----
>>> board = [["o","a","a","n"],
...          ["e","t","a","e"],
...          ["i","h","k","r"],
...          ["i","f","l","v"]]
>>> words = ["oath","pea","eat","rain"]
>>> Solution().findWords(board, words)
['oath', 'eat']

解题思路
--------
使用 Trie（前缀树） + DFS 回溯：
1. 将所有单词构建成 Trie，每个节点存储子节点和以该节点为结尾的单词。
2. 遍历棋盘每个单元格，从 Trie 根节点出发进行 DFS。
3. DFS 时沿 Trie 向下匹配，遇到完整单词就记录结果。
4. 用 '#' 原地标记已访问单元格，回溯时恢复原字符。
5. 搜索后剪枝 Trie 末端节点（删除无子节点路径），减少后续重复搜索。
"""

# first define the Trie class to hold each char in a word

class Trie(object):
    def __init__(self) -> None:
        self.children = {}
        self.word = None

class Solution(object):
    """
    解法复杂度分析
    --------------

    记棋盘大小为 m x n，所有单词中字符总数为 L，最长单词长度为 L_max。

    时间复杂度: O(L + m * n * 3^L_max)
        - 构建 Trie: O(L)              — 每个字符插入一次
        - DFS 搜索:  O(m * n * 3^L_max) — 每个单元格作为起点，
          最多沿 Trie 深度 L_max 搜索，分支因子最大为 3
          （因已访问单元格不能重复，每个单元格最多 3 个未访邻）。
        - Trie 剪枝在平均情况下显著降低实测耗时，
          但最坏情况（如全相同字符 + Trie 含匹配前缀）仍为指数上界。

    空间复杂度: O(L)
        - Trie 结构: O(L)              — 存所有单词字符
        - DFS 递归栈: O(L_max)          — 递归深度 = 最长单词
        - 结果列表:   O(K)              — K 为找到的单词数
        - 棋盘标记:   O(1)              — 原地 '#' 标记，无额外矩阵

    关键优化
    --------
    1. Trie 剪枝: 仅沿存在字符的路径延伸，避免盲目搜索。
    2. 叶节点删除: 搜索后移除 Trie 末端空节点，缩小后续搜索空间。
    3. 原地标记:   使用 '#' 而非 visited 矩阵，省去 O(m*n) 空间。
    """

    def findWords(self, board, words):
        # 边界情况处理：空 board 或空 words 直接返回
        if not board or not board[0] or not words:
            return []
        # build the word Tries
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
    # 测试 1：官方示例
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    print("测试 1:", Solution().findWords(board, words))  # 期望: ['oath', 'eat']

    # 测试 2：空 board 边界
    print("测试 2 (空 board):", Solution().findWords([], ["oath"]))  # 期望: []

    # 测试 3：空 words 边界
    print("测试 3 (空 words):", Solution().findWords(board, []))  # 期望: []

    # 测试 4：单词在多个位置出现（应去重）
    board2 = [["a","a"],["a","a"]]
    words2 = ["aaa"]
    print("测试 4 (去重):", Solution().findWords(board2, words2))  # 期望: ['aaa']