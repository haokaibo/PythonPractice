"""
Tests for Container With Most Water.

Run with:  pytest tests/leetcode/two_pointers/container_with_most_water_test.py -v
"""

import pytest

from src.leetcode.two_pointers.container_with_most_water import maxArea


test_cases = [
    # (height, expected)
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1),
    ([1, 2, 3, 4, 5], 6),
    ([5, 4, 3, 2, 1], 6),
    ([2, 3, 10, 5, 7, 8], 24),
    ([1, 2, 1], 2),
    ([2, 1], 1),
    ([1, 2, 4, 3], 4),
]


@pytest.mark.parametrize("height, expected", test_cases)
def test_max_area(height, expected):
    assert maxArea(height) == expected


def test_example_1():
    """LeetCode example 1."""
    assert maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_example_2():
    """LeetCode example 2."""
    assert maxArea([1, 1]) == 1


def test_all_same_heights():
    """Identical lines — max area is width * height."""
    assert maxArea([5, 5, 5, 5]) == 15
