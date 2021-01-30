class Node:
    def __init__(self, val, nxt=None, pre=None):
        self.val = val
        self.nxt = nxt
        self.pre = pre
        if nxt is not None:
            nxt.pre = self
        if pre is not None:
            pre.nxt = self

    def __str__(self):
        return f'({str(self.val)})'


