"""
Question Description
--------------------
You are asked to implement a Doubly Linked List. Each node in a doubly
linked list has a "value" plus pointers to the "next" and "previous" (prev)
nodes in the list.

The linked list class (LinkedList) must support the following operations:

    1. setHead(node)     -> Insert a node at the head (front) of the list.
    2. setTail(node)     -> Insert a node at the tail (end) of the list.
    3. insertBefore(node, nodeToInsert)
        -> Insert nodeToInsert immediately before the given node in the list.
    4. insertAfter(node, nodeToInsert)
        -> Insert nodeToInsert immediately after the given node in the list.
    5. insertAtPosition(position, nodeToInsert)
        -> Insert nodeToInsert at the given 1-indexed position. Position 1 is
           the head, position 2 is the second node, etc.
    6. remove(node)
        -> Remove the given node (by reference) from the list.
    7. removeNodesWithValue(value)
        -> Remove all nodes that have a value equal to the given value.
    8. containsNodeWithValue(value)
        -> Return True if any node in the list has the given value, else False.

Example:

    # Build list: 1 <-> 2 <-> 3
    head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    ll = LinkedList()
    ll.setHead(head)
    ll.setTail(node3)
    ll.insertBefore(node3, node2)

    ll.insertAtPosition(1, Node(0))      # -> 0 <-> 1 <-> 2 <-> 3
    ll.removeNodesWithValue(2)            # -> 0 <-> 1 <-> 3
    ll.containsNodeWithValue(3)         # -> True
    ll.containsNodeWithValue(2)         # -> False

Time Complexity (per operation):
    - setHead / setTail / insertBefore / insertAfter / insertAtPosition:
      O(1) for head/tail inserts; O(position) for insertAtPosition which may
      walk the list from the head to the desired position.
    - remove (by reference): O(1) - we already have the node reference.
    - removeNodesWithValue: O(n) - we must traverse the entire list.
    - containsNodeWithValue: O(n) - we must traverse the entire list.

Space Complexity: O(1) per operation.
    No additional data structures proportional to the input are used; we only
    manipulate node pointers in place. The list itself stores n Node objects,
    which is the representation of the input, not auxiliary space.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # 1. Set a node as the head of the list.
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    # 2. Set a node as the tail of the list.
    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    # 3. Insert nodeToInsert immediately before the given node.
    def insertBefore(self, node, nodeToInsert):
        self.removeNodePointers(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is not None:
            node.prev.next = nodeToInsert
        else:
            self.head = nodeToInsert
        node.prev = nodeToInsert

    # 4. Insert nodeToInsert immediately after the given node.
    def insertAfter(self, node, nodeToInsert):
        self.removeNodePointers(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is not None:
            node.next.prev = nodeToInsert
        else:
            self.tail = nodeToInsert
        node.next = nodeToInsert

    # 5. Insert nodeToInsert at a 1-indexed position.
    def insertAtPosition(self, position, nodeToInsert):
        if position <= 1:
            self.setHead(nodeToInsert)
            return
        current = self.head
        pos = 1
        while current is not None and pos < position:
            current = current.next
            pos += 1
        if current is None:
            self.setTail(nodeToInsert)
        else:
            self.insertBefore(current, nodeToInsert)

    # 6. Remove the given node (by reference) from the list.
    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodePointers(node)

    # Helper to detach a node from any existing list links.
    def removeNodePointers(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    # 7. Remove all nodes whose value equals the given value.
    def removeNodesWithValue(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                target = current
                current = current.next
                self.remove(target)
            else:
                current = current.next

    # 8. Check whether a node with the given value exists in the list.
    def containsNodeWithValue(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False
