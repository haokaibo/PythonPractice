class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class SwapPairs:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        next = head.next
        if next.next is not None:
            head.next = self.swapPairs(next.next)
        else:
            head.next = None
        next.next = head
        return next

    def buildPairs(self, arr: []) -> ListNode:
        head = None
        current = None
        for a in arr:
            if head is None:
                head = ListNode(a)
                current = head
            else:
                current.next = ListNode(a)
                current = current.next
        return head

    def printPairs(self, head: ListNode):
        while head is not None:
            print(f'{head.val}')
            head = head.next


if __name__ == '__main__':
    swap_pairs = SwapPairs()
    head = swap_pairs.buildPairs([1, 2, 3, 4])
    swap_pairs.printPairs(head)

    head = swap_pairs.swapPairs(head)
    swap_pairs.printPairs(head)
