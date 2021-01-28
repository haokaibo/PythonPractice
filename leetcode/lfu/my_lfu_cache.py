from leetcode.lfu import CacheNode
from leetcode.lfu import FreqNode


class LFUCache(object):
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.freq_link_head = None

    def get(self, key):
        if key in self.cache:
            cache_node = self.cache[key]
            self.move_forward(cache_node)
            return cache_node.value
        else:
            return None

    def set(self, key, value):
        if self.capacity <= 0:
            return None

        if key not in self.cache:
            if len(self.cache) >= self.capacity:
                self.dump_cache()
            self.create_cache(key, value)
        else:
            cache_node = self.cache[key]
            cache_node.value = value
            self.move_forward(cache_node)

    def move_forward(self, cache_node: CacheNode):
        freq_node = cache_node.freq_node
        if freq_node.nxt is None or freq_node.nxt.freq != freq_node.freq + 1:
            target_freq_node = FreqNode(freq_node.freq + 1, None, None)
            target_empty = True
        else:
            target_freq_node = freq_node.nxt
            target_empty = False

        # read here
        cache_node.free_myself()
        target_freq_node.append_cache_to_tail(cache_node)

        if target_empty:
            freq_node.insert_after_me(target_freq_node)
        if freq_node.count_caches() == 0:
            if self.freq_link_head == freq_node:
                self.freq_link_head =target_freq_node
            freq_node.remove()

    def dump_cache(self):
        head_freq_node = self.freq_link_head
        self.cache.pop(head_freq_node.cache_head.key)
        head_freq_node.pop_head_cache()

        if head_freq_node.count_caches() == 0:
            self.freq_link_head = head_freq_node.nxt
            head_freq_node.remove()