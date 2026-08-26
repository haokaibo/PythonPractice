"""
LeetCode 2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a
linked list.

You may assume the two numbers do not contain any leading zero, except
the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
1. The adding requires to iterate to the tail of each ListNode first
2. Use two intergers to hold the digits e.g. n1 = l1.val * pow(10, digit_pos) + n1
3. Sum the n1 and n2
4. Use a listNode to hold the digits of the sum
e.g. 
7243 + 564 = 7807
"""


class Solution(object):
    def revertListNode(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    """
    Time: O(n), Space: O(n)
    """
    def addNumbersByListNode(self, l1, l2):
        reversed_l1 = self.revertListNode(l1)
        reversed_l2 = self.revertListNode(l2)

        extra = 0   
        current = previous = None
        while reversed_l1 or reversed_l2 or extra:
            n1 = reversed_l1.val if reversed_l1 else 0
            n2 = reversed_l2.val if reversed_l2 else 0

            plain_sum = n1 + n2 + extra
            extra = plain_sum // 10

            current = ListNode(plain_sum % 10, previous)
            previous = current

            if reversed_l1: reversed_l1 = reversed_l1.next
            if reversed_l2: reversed_l2 = reversed_l2.next

        return 0 if current is None else current
            

    def convertListNodeToNum(self, l):
        digits = []
        while l is not None:
            digits.append(str(l.val))
            l = l.next
        
        num_str = "".join(digits)
        return 0 if len(num_str) == 0 else int(num_str)
        
    def addNumersByList(self, l1, l2):
        n1 = self.convertListNodeToNum(l1)
        n2 = self.convertListNodeToNum(l2)
            
        plain_sum = n1 + n2
        
        if plain_sum == 0:
            return ListNode(plain_sum)
        
        current = previous = None
        
        while plain_sum > 0:
            current = ListNode(plain_sum % 10, previous)
            previous = current
            plain_sum = plain_sum // 10
            
        return current    
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # return self.addNumersByList(l1, l2)  
        return self.addNumbersByListNode(l1, l2)
            

def buildListNode(num_str):
    head = None
    previous = None
    for s in num_str:
        current = ListNode(int(s))
        if head is None:
            head = current
        else:
            previous.next = current
        previous = current

    return head

def printListNode(l):
    while l is not None:
        print(f"{l.val}->")
        l=l.next

if __name__ == "__main__":
    # l1 = buildListNode("5")
    # l2 = buildListNode("5")
    # printListNode(Solution().addTwoNumbers(l1, l2))
    nodes = [ListNode(1, ListNode(2)), ListNode(3, ListNode(4))]
    nodes[1] = nodes[1].next
    for n in nodes:
        print(n.val)
        