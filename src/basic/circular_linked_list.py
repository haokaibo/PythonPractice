from basic.node import Node


class CircularLinkedList:
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def add(self, val):
        if self.size == 0:
            self.root = Node(val)
            self.root.nxt = self.root
        else:
            node = Node(val, self.root.nxt, pre=self.root)
            self.root.nxt = node
        self.size += 1
        return self

    def find(self, val):
        node = self.root
        while node is not None:
            if val == node.name:
                return node
            else:
                node = node.nxt
                if node == self.root:
                    break
        return False

    def remove(self, val):
        node = self.root
        while node is not None:
            if node.name == val:
                node.nxt.pre = node.pre
                if node == self.root:
                    node.pre.nxt = node.nxt
                    node.nxt.pre = node.pre
                    self.root = node.nxt
                else:
                    node.pre.nxt = node.nxt
                self.size -= 1
                node.pre = node.nxt = None
                return True
            else:
                node = node.nxt
                if node == self.root:
                    break
        return False

    def print_list(self):
        node = self.root
        while node is not None:
            print(node, end='->')
            node = node.nxt
            if node == self.root:
                break
        print()