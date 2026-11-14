"""
Difficulty:
Category: Famous Algorithms Successful Submissions: 3,782+
Union Find •
The union-find data structure is similar to a traditional set data structure in that it contains a collection of unique values. However, these values are spread out amongst a variety of distinct disjoint sets, meaning that no set can have duplicate values, and no two sets can contain the same value.
Write a
UnionFind class that implements the union-find (also called a disjoint set) data structure. This
class should support three methods:
createSet(value) : Adds a given value in a new set containing only that value.
union (valueOne, valueTwo) : Takes in two values and determines which sets they are in. If they are in different sets, the sets are combined into a single set. If either value is not in a set or they are in the same set, the function should have no effect.
• find(value) : Returns the "representative" value of the set for which a value belongs to. This can be any value in the set, but it should always be the same value, regardless of which value in the set find is passed. If the value is not in a set, the function should return null / None .
Note that after a set is part of a union, its representative can potentially change.
You can assume
createSet
will never be called with the same value twice.
If you're unfamiliar with Union Find, we recommend watching the Conceptual Overview section of this question's video explanation before starting to code.
Sample Usage

createSet (5): null
createSet(10): null
find(5): 5
find (10): 10
union (5, 10): null
find (5): 5
find (10): 5
createSet (20): null
"""

class UnionFind:
    def __init__(self):
        # 记录每个节点对应的父节点
        self.parent = {}
        # 可选：记录树的秩（深度）或大小，用于按秩合并

    def createSet(self, value):
        # 每个新值自成一个集合，父节点指向自己
        self.parent[value] = value

    def find(self, value):
        if value not in self.parent:
            return None
        
        # 路径压缩（Path Compression）：
        # 如果当前节点不是根节点，递归找到根节点，并把路径上的节点直接连到根上
        if self.parent[value] != value:
            self.parent[value] = self.find(self.parent[value])
        
        return self.parent[value]

    def union(self, valueOne, valueTwo):
        rootOne = self.find(valueOne)
        rootTwo = self.find(valueTwo)

        # 如果任一值不存在，或已经在同一个集合中，则什么都不做
        if rootOne is None or rootTwo is None:
            return
        
        # 将一棵树的根挂到另一棵树的根下
        self.parent[rootOne] = rootTwo