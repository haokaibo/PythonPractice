"""
LeetCode 206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the
reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = []
Output: []
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Solution A(Iteration: 
1. Use the iteration method to iterate the singly-linked list.
2. Use previous and current pointers to hold the iterated nodes
    current.next = previous
    
"""
class Solution(object):
    def reverseListRecursively(self, current):
        """
        1. Look for the tail by recusively calling
        2. Return the tail as new head
        3. current.next.next = current

        """
        if current is None:
            return None
        
        
        new_head = self.reverseListRecursively(current.next)

        if new_head is None: # The current is the tail / new head
            new_head = current
        else:
            # middle node
            current.next.next = current
            current.next = None

        return new_head

    def reverseListIteratively(self, head):
        previous = head
        current = head.next
        previous.next = None
        
        while current is not None:
            next = current.next
            current.next = previous
            if next is None:
                break
            previous = current
            current = next

        return current


    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        return self.reverseListRecursively(head)
        

if __name__ == "__main__":

    previous = None
    current = None
    for i in range(5, 0, -1):
        current = ListNode(i, previous)
        previous = current

    current = Solution().reverseList(current)
    while current is not None:
        print(current.val)
        current = current.next