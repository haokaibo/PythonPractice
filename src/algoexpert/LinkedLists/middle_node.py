# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    # Write your code here.
    # Solution
    # Use slow and fast pointers to iterate the linkedList. 
    # The middle node can be known when the iteration is complete.
    # Slow pointer move 1 node, fast pointer move 2 nodes for each iteration.
    # If the fast pointer reaches the end perfectly, then there is even nodes, the slow pointer is pointing to the previous node of the middle node
    # else the slow pointer is pointing to the middle node
    # Time complexity: O(n)
    # Space complexity: O(1)
    
    # e.g. 
    # 1 -> 2 -> 3
    # S    F
    #      S    F
    # M = S

    # e.g. 
    # 1 -> 2 -> 3 -> 4
    # S    F
    #      S         F
    # M = S.next

    if linkedList is None:
        return None
    slow = linkedList
    fast = slow.next

    # 1
    # 1 -> 2
    # 1 -> 2 -> 3
    # S    F    
    #      S    F
    # 1 -> 2 -> 3 -> 4
    # S    F      
    #      S         F 
    while fast is not None:
        if fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        else:
            break

    # when fast is None, it means there is Odd nodes.
    middle = slow if fast is None else slow.next

    return middle

