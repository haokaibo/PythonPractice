# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class UniqueBinaryTreeII:

    def generateTrees(self, n: int) -> List[TreeNode]:
        def push(root, node):
            if node is None or root is None:
                return
            if node.val >= root.val:
                push(root.right, node)
            else:
                push(root.left, node)

        trees: List[TreeNode] = []

        for i in range(1, n + 1):
            root = TreeNode(i)
            trees.append(root)
            for j in range(1, n+1):
                push(root, TreeNode(j))
        return trees

    def iterate_tree_to_list(self, root, list:List[int]):
        if root is None:
            list.append(root)
            return
        else:
            list.append(root.val)
            self.iterate_tree_to_list(root.left, list)
            self.iterate_tree_to_list(root.right, list)



if __name__ == '__main__':
    uniqueBinaryTreeII = UniqueBinaryTreeII()
    trees= uniqueBinaryTreeII.generateTrees(3)
    list=[]
    for tree in trees:
        print(uniqueBinaryTreeII.iterate_tree_to_list(tree,list))
