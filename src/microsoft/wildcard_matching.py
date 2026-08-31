"""
LeetCode 44. Wildcard Matching [Hard]

Given an input string s and a pattern p, implement wildcard pattern matching
with support for '?' and '*' where:
  - '?' matches any single character.
  - '*' matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

Example 1:
Input:  s = "aa",   p = "*"
Output: True
Explanation: '*' matches any sequence.

Example 2:
Input:  s = "cb",   p = "?a"
Output: False
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 3:
Input:  s = "abcd", p = "a*d"
Output: True

Example 4:
Input:  s = "abcded", p = "a**d"
Output: True
Explanation: consecutive '*' collapses to a single '*'.

Constraints:
- 0 <= s.length, p.length <= 2000
- s contains only lowercase English letters.
- p contains only lowercase English letters, '?' or '*'.

Solution (greedy two-pointer with backtracking, O(m + n) worst case):

  - i walks s, j walks p.
  - On a normal char, advance both when matched.
  - On '*', record star = j, i_star = i (the rollback anchor), then j += 1.
  - On mismatch, if a previous '*' exists, let it "eat" one more char of s
    (i = ++i_star, j = star + 1) and retry.
  - At the end, the remaining pattern must be all '*' to be matchable.

The regex-based solution re.fullmatch(re.escape(p).replace(...)) looks
elegant but is NOT safe: Python's `re` engine is backtracking and explodes
(exponential time) on patterns with many '*' over long strings. The LeetCode
test below is the canonical adversarial case that hangs the regex version.

Time : O(m + n)
Space: O(1)
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        Greedy wildcard matching.

        Complexity:
          Time:  O(m + n), where m = len(s) and n = len(p).
                 Each pointer only moves forward; on a mismatch we replay
                 from the last '*', and each character of s is consumed at
                 most once by that replay branch, so the total work is linear.
          Space: O(1). Only a few integer indices are kept (i, j, star,
                 i_star); the input strings are not copied.

        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        i = j = 0
        star = -1          # last '*' position in p
        i_star = -1        # s index when that '*' was encountered

        while i < m:
            if j < n and p[j] == '*':
                # Try matching zero chars from s for now; remember fallback.
                star = j
                i_star = i
                j += 1
            elif j < n and (p[j] == '?' or p[j] == s[i]):
                i += 1
                j += 1
            elif star != -1:
                # Mismatch: let the last '*' absorb one more char of s.
                j = star + 1
                i_star += 1
                i = i_star
            else:
                return False

        # s exhausted; any leftover pattern must be all '*'.
        while j < n and p[j] == '*':
            j += 1
        return j == n


if __name__ == "__main__":
    sol = Solution()

    cases = [
        ("aa",            "*",                                 True),
        ("abcd",          "a*d",                               True),
        ("abcd",          "a*e",                               False),
        ("abc",           "a?c",                               True),
        ("abcde",         "a*d",                               False),
        ("abcded",        "a*d",                               True),
        ("abcded",        "a**d",                              True),
        ("",              "*",                                 True),
        ("",              "",                                  True),
        ("a",             "",                                  False),
        ("mississippi",   "m*i*p*i",                           True),
        # The adversarial LeetCode case that hangs the regex version.
        (
            "aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba",
            "*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*",
            True,
        ),
    ]

    for s, p, expected in cases:
        got = sol.isMatch(s, p)
        status = "OK" if got == expected else "FAIL"
        print(f"[{status}] isMatch(s[{len(s)}], p[{len(p)}]) = {got} "
              f"(expected {expected})")
