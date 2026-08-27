"""
LeetCode 133. Clone Graph

You are given a representation of a connected undirected graph. Return a deep
copy (clone) of the graph. Each node's value is unique and matches its index
in the adjacency list.

Example 1:
Input: adj = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]

Example 2:
Input: adj = [[]]
Output: [[]]

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
"""
Solution:
1. To deep copy a graph, each node in the graph should be iterated once, and all its neighbors should be visited.
2. each node's value is the same as the node's index -> use a dict [old nth node.val: new nth node]
3. Refer the dict to build the new graph
4. Stop condition: when all the nodes and their neighbors are in the dict the iteration is done

Time: O(n), Space: O(n)
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        new_node = None
        if not node.neighbors:
            new_node = Node(node.val, None)
            return new_node
        
        stack = [node]
        new_dict = dict()
        while len(stack) > 0:
            old = stack.pop()
            if old.val not in new_dict:
                new_dict[old.val] = Node(old.val)
            
            for n in old.neighbors:
                if n.val not in new_dict:
                    stack.append(n)
                    new_dict[n.val] = Node(n.val)
                new_dict[old.val].neighbors.append(new_dict[n.val])
                
        return new_dict[1]
                
                
            
                