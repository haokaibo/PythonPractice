class ValueNode:
    def __init__(self, val, freq_node=None, pre=None, nxt=None):
        self.val = val
        self.freq_node = freq_node
        self.pre = pre
        self.nxt = nxt
        if self.freq_node is not None:
            if self.freq_node.value_head is None:
                self.freq_node.value_head = self.freq_node.value_tail = self
            else:
                self.freq_node.value_tail.nxt = self
                self.pre = self.freq_node.value_tail
                self.freq_node.value_tail = self

    def free_me(self):
        if self.freq_node is None:
            return False

        if self.freq_node.value_head == self.freq_node.value_tail:
            self.freq_node.value_head = self.freq_node.value_tail = None
        elif self.freq_node.value_head == self:
            self.freq_node.value_head = self.nxt
            if self.nxt is not None:
                self.nxt.pre = None
        elif self.freq_node.value_tail == self:
            self.freq_node.value_tail = self.pre
            self.pre.nxt = None
        else:
            self.pre.nxt = self.nxt
            self.nxt.pre = self.pre
        self.pre = self.nxt = None
        self.freq_node = None

        return True


class FreqNode:
    def __init__(self, freq, nxt=None, pre=None):
        self.freq = freq
        self.value_head = None
        self.value_tail = None
        self.nxt = nxt
        self.pre = pre
        if self.nxt is not None:
            self.nxt.pre = self
        if self.pre is not None:
            self.pre.nxt = self

    def add_value_node(self, value_node):
        if self.value_head is None:
            self.value_head = self.value_tail = value_node
        else:
            self.value_tail.nxt = value_node
            value_node.pre = self.value_tail
            self.value_tail = value_node
        value_node.freq_node = self


class FrequentCache:
    def __init__(self):
        self.dic = dict()
        self.freq_head = None
        self.freq_tail = None

    def add(self, fn):
        if self.freq_head is None and self.freq_tail is None:
            self.freq_head = self.freq_tail = fn
        elif self.freq_head is not None and self.freq_head.freq != 1:
            self.freq_head.pre = fn
            fn.nxt = self.freq_head
            self.freq_head = fn

    def visit(self, v):
        if v not in self.dic:
            # if there is no freq=1 node in the freq queue
            if self.freq_head is None or self.freq_head.freq != 1:
                freq_node = FreqNode(1)
                self.add(freq_node)
            freq_node = self.freq_head
            value_node = ValueNode(v, freq_node)
            self.dic[v] = value_node
        else:
            value_node = self.dic[v]
            freq_node = value_node.freq_node
            if freq_node.nxt is None or (freq_node.nxt.freq - 1 != freq_node.freq):
                new_freq_node = FreqNode(freq_node.freq + 1, freq_node.nxt, freq_node)
                if new_freq_node.nxt is None:
                    self.freq_tail.nxt = new_freq_node
                    new_freq_node.pre = self.freq_tail
                    self.freq_tail = new_freq_node
            else:
                new_freq_node = freq_node.nxt

            value_node.free_me()
            new_freq_node.add_value_node(value_node)

    def get_k_most_frequent_visit_items(self, k):
        result = {}
        i = 0
        curr_node = self.freq_tail
        while i < k and curr_node is not None:
            result[curr_node.freq] = []
            v_node = curr_node.value_head
            while v_node is not None:
                result[curr_node.freq].append(v_node.val)
                v_node = v_node.nxt
            curr_node = curr_node.pre
            i += 1
        return result


fc = FrequentCache()
for i in range(5):
    fc.visit(i)
for i in range(3):
    fc.visit(i)

print(fc.get_k_most_frequent_visit_items(3))
