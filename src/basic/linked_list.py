from basic.node import Node


class LinkedList:
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def add(self, val):
        new_node = Node(val, self.root)
        self.root = new_node
        self.size += 1
        return self

    def find(self, val):
        node = self.root
        while node is not None:
            if val == node.name:
                return node
            else:
                node = node.nxt
        return None

    def remove(self, val):
        node = self.root
        while node.nxt is not None:
            if node.name == val:
                node.nxt.pre = node.pre
                if node == self.root:
                    self.root = node.nxt
                else:
                    node.pre.nxt = node.nxt
                self.size -= 1
                node.pre = node.nxt = None
                return True
            else:
                node = node.nxt
        return False

    def print_list(self):
        node = self.root
        while node is not None:
            print(node, end='->')
            node = node.nxt
        print('None')
