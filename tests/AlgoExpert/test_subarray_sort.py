"""
Tests for Subarray Sort (AlgoExpert - Arrays).

Run with:  pytest tests/AlgoExpert/test_subarray_sort.py -v
"""

import pytest

from src.algoexpert.Arrays.subarray_sort import subarraySort


test_cases = [
    # (array, expected)
    ([1, 2, 4, -2, 5, 7, 8], [0, 3]),
    ([2, 4, 5, 7, 3, 6, 8], [1, 5]),
    ([1, 2, 3, 4, 5], [-1, -1]),
    ([1, 2, 3, 6, 4, 5], [3, 5]),
    ([5, 4, 3, 2, 1], [0, 4]),
    ([1, 3, 2, 4, 5], [1, 2]),
    ([-1, 1, 2, 3, 4, 5], [-1, -1]),
    ([1, 2, 3, 4, 5, 4], [4, 5]),
]


@pytest.mark.parametrize("array, expected", test_cases)
def test_subarray_sort(array, expected):
    assert subarraySort(array) == expected


def test_example_1():
    """Array with a dip in the middle."""
    assert subarraySort([1, 2, 4, -2, 5, 7, 8]) == [0, 3]


def test_already_sorted():
    assert subarraySort([1, 2, 3, 4, 5]) == [-1, -1]


def test_single_element():
    assert subarraySort([42]) == [-1, -1]


def test_negative_numbers():
    assert subarraySort([-1, 1, 2, 3, 4, 5]) == [-1, -1]


def test_entire_array_unsorted():
    """Reverse-sorted array — whole thing must be sorted."""
    assert subarraySort([5, 4, 3, 2, 1]) == [0, 4]
