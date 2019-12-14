class ListNode:
    def __init__(self, value):
        self.value =value
        self.next = None


class ReverseLinkList:
    def reverseList(self, head: ListNode) -> ListNode:
        def helper(previous: ListNode, current: ListNode) -> ListNode:
            if current is None:
                new_head = previous
            else:
                new_head = helper(current, current.next)
                current.next = previous
            return new_head

        new_head = helper(None, head)
        return new_head

    def printLinkList(self, head: ListNode):
        while head is not None:
            print(head.value)
            head=head.next

    def buildLinkList(self, arr: []):
        head = ListNode(arr[0])
        current = head
        for i in range(1, len(arr)):
            current.next= ListNode(arr[i])
            current=current.next
        return head

if __name__ == '__main__':
    rll = ReverseLinkList()
    head = rll.buildLinkList([1,2,3,4,5])
    head = rll.reverseList(head)
    rll.printLinkList(head)