from unittest import TestCase

from leetcode.lfu.my_lfu_cache import MyLFUCache


class LFUCacheTest(TestCase):
    def test_lfu_cach(self):
        lfu_cache = MyLFUCache(2)
        lfu_cache.set(1, 1)
        lfu_cache.set(2, 2)
        assert (lfu_cache.get(1) == 1)  # 返回

        lfu_cache.set(3, 3)  # 去除键
        assert (lfu_cache.get(2) == -1)  # 返回 - 1（未找到）
        assert (lfu_cache.get(3) == 3)  # 返回 3

        lfu_cache.set(4, 4)  # 去除键
        assert (lfu_cache.get(1) == -1)  # 返回 - 1（未找到）
        assert (lfu_cache.get(3) == 3)  # 返回
        assert (lfu_cache.get(4) == 4)  # 返回
