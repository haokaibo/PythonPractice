"""
Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.

Example 2:
    Input: s = "cbbd"
    Output: "bb"

Constraints:
    - 1 <= s.length <= 1000
    - s consists of only digits and English letters.
"""

from typing import List


def longest_palindrome(s: str) -> str:
    """
    Optimized Solution: Time: O(n^2), Space: O(1)

    Strategy:
    1. Expand Around Center: a palindrome mirrors around its center.
       There are 2n-1 possible centers (each character + each gap between
       two characters).
    2. For each center, expand outward while the characters match.
    3. Track the start and end indices of the longest palindrome found.

    Key insight:
    - Rather than checking every substring (O(n^3)), we expand from each
      center only when needed. Two characters expand from a single
      center (odd-length palindromes) and two adjacent centers expand
      from a gap (even-length palindromes).
    - A helper function handles both odd and even lengths cleanly.

    Time complexity  : O(n^2) — for each of up to 2n-1 centers we may
                       expand up to O(n) times.
    Space complexity : O(1) — only index variables are used (the result
                       substring slice is part of the output).
    """
    if not s:
        return ""

    def expand_around_center(left: int, right: int) -> int:
        """Return the length of the palindrome centered between left/right."""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # When the loop exits the bounds are exclusive, so the palindrome
        # length is (right - left - 1).
        return right - left - 1

    start = 0
    end = 0

    for i in range(len(s)):
        # Odd-length palindrome (single character center)
        len1 = expand_around_center(i, i)
        # Even-length palindrome (between i and i+1)
        len2 = expand_around_center(i, i + 1)

        current_len = max(len1, len2)
        if current_len > end - start:
            # Recompute the start index from the center and length
            start = i - (current_len - 1) // 2
            end = i + current_len // 2

    return s[start:end + 1]


# Example usage and test cases
if __name__ == "__main__":
    # Test case 1: LeetCode example
    s1 = "babad"
    result1 = longest_palindrome(s1)
    print(f"Test 1 - s: \"{s1}\"")
    print(f"Longest palindrome: \"{result1}\" (expected: \"bab\" or \"aba\")")
    print()

    # Test case 2: Even-length palindrome
    s2 = "cbbd"
    result2 = longest_palindrome(s2)
    print(f"Test 2 - s: \"{s2}\"")
    print(f"Longest palindrome: \"{result2}\" (expected: \"bb\")")
    print()

    # Test case 3: Single character
    s3 = "a"
    result3 = longest_palindrome(s3)
    print(f"Test 3 - s: \"{s3}\"")
    print(f"Longest palindrome: \"{result3}\" (expected: \"a\")")
    print()

    # Test case 4: Whole string is a palindrome
    s4 = "racecar"
    result4 = longest_palindrome(s4)
    print(f"Test 4 - s: \"{s4}\"")
    print(f"Longest palindrome: \"{result4}\" (expected: \"racecar\")")
    print()

    # Test case 5: No repeated characters
    s5 = "abcdef"
    result5 = longest_palindrome(s5)
    print(f"Test 5 - s: \"{s5}\"")
    print(f"Longest palindrome: \"{result5}\" (expected: \"a\")")
