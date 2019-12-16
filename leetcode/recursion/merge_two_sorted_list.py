# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MergeTwoSortedList:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        result = None
        if l1.val <= l2.val:
            result = l1
            l1 = l1.next
        else:
            result = l2
            l2 = l2.next

        result.next = self.mergeTwoLists(l1, l2)
        return result

if __name__ =='__main__':
    l1 =ListNode(1)
    l1.next=ListNode(2)
    l1.next.next=ListNode(4)
    l2 =ListNode(1)
    l2.next=ListNode(3)
    l2.next.next=ListNode(4)
    merged = MergeTwoSortedList().mergeTwoLists(l1, l2)
    while merged is not None:
        print(merged.val)
        merged=merged.next