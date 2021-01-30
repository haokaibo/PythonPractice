from basic.node import Node


class DoublyLinkedList:
    def __init__(self, r=None):
        self.head = r
        self.tail = r
        self.size = 0

    def add(self, val):
        if self.size == 0:
            self.head = self.tail = Node(val)
        else:
            node = Node(val, nxt=self.head)
            self.head = node
        self.size += 1

    def find(self, val):
        node = self.head
        while node is not None:
            if node.val == val:
                return node
            else:
                node = node.nxt
        return False

    def remove(self, val):
        node = self.head
        while node is not None:
            if node.val == val:
                if self.head == self.tail:
                    self.head = self.tail = None
                elif self.head == node:
                    self.head = node.nxt
                    node.nxt.pre = node.pre
                    node = None
                elif self.tail == node:
                    self.tail = node.pre
                    node.pre.nxt = None
                    node = None
                else:
                    node.nxt.pre = node.pre
                    node.pre.nxt = node.nxt
                    node = None
                self.size -= 1
                return True
            else:
                node = node.nxt
        return False

    def print_list(self):
        node = self.head
        while node is not None:
            print(node, end='->')
            node = node.nxt
        print()
