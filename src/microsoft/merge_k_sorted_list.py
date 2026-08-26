"""
LeetCode 23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted
in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Example 2:
Input: lists = []
Output: []
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
1. Iterate the all the sorted list item by item.
2. check the min of each num in the k elements.
3. Build a new list to hold the minimal element.
"""
class Solution(object):
    def check_minimal_item_list(self, k_heads):
        minimal_head = None
        minimal_head_index = None
        for index, head in enumerate(k_heads):
            if head is None:
                continue
                
            if minimal_head is None or head.val < minimal_head.val:
                minimal_head = head
                minimal_head_index = index

        if minimal_head_index is not None:
            k_heads[minimal_head_index] = k_heads[minimal_head_index].next

        return minimal_head
    
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        head = current = previous = None

            
        while len(lists) > 0:
            minimal_head = self.check_minimal_item_list(lists)
            if minimal_head is None:
                break
                
            current = ListNode(minimal_head.val)
            
            if head is None:
                head = current
            if previous is not None:
                previous.next = current
            previous = current
            
            
        return head
            
def printListNode(l):
    output = []
    while l is not None:
        output.append(l.val)
        l = l.next
    print(" -> ".join(map(str,output)))

if __name__ == "__main__":
    val_lists = [[1,4,5],[1,3,4],[2,6]]
    lists = []
    for values in val_lists:
        head = current = previous = None
        for v in values:
            current = ListNode(v)
            if head is None:
                head = current
            if previous is not None:
                previous.next = current
            previous = current
        lists.append(head)
        printListNode(head)
    result = Solution().mergeKLists(lists)

