class FreqNode(object):
    """
    doubly linked list
    """

    def __init__(self, freq, pre, nxt):
        self.freq = freq
        self.pre = pre  # previous FreqNode
        self.nxt = nxt  # next FreqNode
        self.cache_head = None  # CacheNode head under this FreqNode
        self.cache_tail = None  # CacheNode tail under this FreqNode

    def count_caches(self):
        if self.cache_head is None and self.cache_tail is None:
            return 0
        elif self.cache_head == self.cache_tail:
            return 1
        else:
            return '2+'

    def remove(self):
        if self.pre is not None:
            self.pre.nxt = self.nxt
        if self.nxt is not None:
            self.nxt.pre = self.pre

        pre = self.pre
        nxt = self.nxt
        self.pre = self.nxt = self.cache_head = self.cache_tail = None

        return (pre, nxt)

    def pop_head_cache(self):
        if self.cache_head is None and self.cache_tail is None:
            return None
        elif self.cache_head == self.cache_tail:
            cache_head = self.cache_head
            self.cache_head = self.cache_tail = None
            return cache_head
        else:
            cache_head = self.cache_head
            self.cache_head.nxt.pre = None
            self.cache_head = self.cache_head.nxt
            return cache_head

    def append_cache_to_tail(self, cache_node):
        cache_node.freq_node = self

        if self.cache_head is None and self.cache_tail is None:
            self.cache_head = self.cache_tail = cache_node
        else:
            cache_node.pre = self.cache_tail
            cache_node.nxt = None
            self.cache_tail.nxt = cache_node
            self.cache_tail = cache_node

    def insert_after_me(self, freq_node):
        freq_node.pre = self
        freq_node.nxt = self.nxt

        if self.nxt is not None:
            self.nxt.pre = freq_node

        self.nxt = freq_node

    def insert_before_me(self, freq_node):
        if self.pre is not None:
            self.pre.nxt = freq_node

        freq_node.pre = self.pre
        freq_node.nxt = self
        self.pre = freq_node