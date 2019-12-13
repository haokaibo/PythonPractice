from unittest import TestCase

from leetcode.binary_search import BinarySearch


class BinarySearchTest(TestCase):
    def test_search(self):
        bs = BinarySearch()
        result = bs.search(nums=[-1, 0, 3, 5, 9, 12], target=9)
        print(result)