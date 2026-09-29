import pytest
from unittest import TestCase


class MinimalHeaviestSetA(TestCase):

    def merge_sort(self):
        pass

    def minimalHeaviestSetA(self, arr):
        pass

    @pytest.mark.skip(reason="No implementation exists yet in src/amazon/. "
                            "This is a stub test awaiting minimalHeaviestSetA().")
    def test1(self):
        a = [4, 2, 5, 1, 6]
        m = MinimalHeaviestSetA()
        assert m.minimalHeaviestSetA(a) == [5, 6]
