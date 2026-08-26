"""
LeetCode 138. Copy List with Random Pointer

A linked list of length n is given such that each node contains an additional
random pointer, which could point to any node in the list, or None.

Construct a deep copy of the list. The deep copy should consist of exactly n
new nodes, where each new node has its value set to the value of its
corresponding original node. Both the next and random pointer of the new
nodes should point to nodes in the copied list.

Example 1:
Input: head = [[7,null],[13,0],[11,1],[10,2],[1,4]]
Output: [[7,null],[13,0],[11,1],[10,2],[1,4]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
Solution:
1. Use an array to hold the random pointers of the orginal nodes, and correpondent new nodes for easy access
2. Iterate the original list to cope the orgin values to new nodes and build the pointers array
3. Iterate the pointers array, to build the random pointers for new copied nodes
Time: O(n), Space: O(n)
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        pointers = []
        new_head = None
        previous = None
        current = None
        
        # use a dict to holde the key value pair of the random:index
        
        index = 0
        origin_nodes = dict()
        while head is not None:
            current = Node(head.val, None, head.random)
            origin_nodes[head] = index
            pointers.append((head.random, current))
            
            if not new_head:
                new_head = current
            if previous:
                previous.next = current
            previous = current
            
            head = head.next
            index += 1
            
        for p in pointers:
            random = p[0]
            if random:
                index = origin_nodes[random]
                p[1].random = pointers[index][1]
                
        return new_head