class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    """
    Question Description
    --------------------
    You are given the head of a singly linked list and an integer k.
    Write a function that removes the kth node from the end of the list.

    - The list is 1-indexed, so k = 1 removes the last node, k = 2 removes
      the second-to-last node, and so on.
    - The head node is guaranteed to have at least k nodes in the list.

    Example:
        head -> 0 -> 1 -> 2 -> 3 -> 4,  k = 4
        -> Removes the node with value 1 (4th from the end).
        Result: 0 -> 2 -> 3 -> 4

    Time Complexity: O(n)
        We use two pointers. The first pointer advances k steps, then both
        pointers move together until the first reaches the end. This scans the
        list at most once, so the total number of node visits is O(n).

    Space Complexity: O(1)
        Only two pointers (first and second) are used; no additional data
        structures are allocated.
    """
    first = head
    second = head

    # 1. first 指针先走 k 步
    for _ in range(k):
        first = first.next

    # 2. 如果 first 走完 k 步变成了 None，说明要删除的是头节点
    if first is None:
        head.value = head.next.value
        head.next = head.next.next
        return

    # 3. first 和 second 同时向前走，直到 first 达到链表末尾
    while first.next is not None:
        first = first.next
        second = second.next

    # 4. 删除 second 的下一个节点
    second.next = second.next.next
