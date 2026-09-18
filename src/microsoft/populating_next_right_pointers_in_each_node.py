class Solution(object):
    def connect(self, root):
        if not root or not root.left:
            return root
        
        # 1. 连接同一个父节点下的左右子节点
        root.left.next = root.right
        
        # 2. 连接跨父节点的相邻子节点（利用父节点已经连好的 next 指针）
        if root.next:
            root.right.next = root.next.left
            
        # 递归处理左右子树
        self.connect(root.left)
        self.connect(root.right)
        
        return root