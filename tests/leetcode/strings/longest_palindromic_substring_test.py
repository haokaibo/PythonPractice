"""
Tests for Longest Palindromic Substring.

Run with:  pytest tests/leetcode/strings/longest_palindromic_substring_test.py -v
"""

import pytest

from src.leetcode.strings.longest_palindromic_substring import longest_palindrome


test_cases = [
    # (s, expected) — for palindromes of length > 1, any valid palindrome is accepted
    ("babad", "bab"),
    ("cbbd", "bb"),
    ("a", "a"),
    ("racecar", "racecar"),
    ("abcdef", "a"),
    ("aa", "aa"),
    ("abcba", "abcba"),
    ("abb", "bb"),
]


@pytest.mark.parametrize("s, expected", test_cases)
def test_longest_palindrome(s, expected):
    """Assert the returned string is a palindrome of the expected length."""
    result = longest_palindrome(s)

    # Must be a palindrome
    assert result == result[::-1]

    # Must be the correct length
    assert len(result) == len(expected)

    # Must exist within the original string
    assert result in s

    # Must actually be a substring of s and a valid palindrome
    assert expected == expected[::-1]


def test_example_1():
    """LeetCode example 1 — both 'bab' and 'aba' are valid."""
    result = longest_palindrome("babad")
    assert result in ("bab", "aba")


def test_example_2():
    """LeetCode example 2."""
    result = longest_palindrome("cbbd")
    assert result == "bb"


def test_empty_string():
    """Edge case — empty input."""
    assert longest_palindrome("") == ""


def test_single_character():
    assert longest_palindrome("x") == "x"
