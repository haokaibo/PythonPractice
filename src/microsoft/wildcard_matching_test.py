"""
Wildcard Matching.

Rules:
  '?' matches any single character.
  '*' matches any sequence of characters (including the empty sequence).

Examples:
  case 1: s = "abcd"  p = "a*d" -> True
  case 2: s = "abcd"  p = "a*e" -> False
  case 3: s = "abc"   p = "a?c" -> True
  case 4: s = "abcde" p = "a*d" -> False
  case 5: s = "abcded" p = "a*d" -> True
  case 6: s = "abcded" p = "a**d" -> True (consecutive '*' collapses to one '*')

Approach: greedy two-pointer with backtracking, O(m + n) worst case.

  - i walks s, j walks p.
  - On a normal char, advance both when matched.
  - On '*', record star = j, i_star = i (the rollback anchor), then j += 1.
  - On mismatch, if a previous '*' exists, let it "eat" one more char of s
    (i = ++i_star, j = star + 1) and retry.
  - At the end, the remaining pattern must be all '*' to be matchable.

The previous regex-based solution re.fullmatch(re.escape(p).replace(...))
looks elegant but is NOT safe: Python's `re` engine is backtracking and
explodes (exponential time) on patterns with many '*' over long strings.
The LeetCode test "aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba" /
"*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*" is the canonical
example that hangs the regex version.
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
        i_star = 0
        star = 0
        while i < m:
            if j < n and p[j] == '*':
                star = j
                i_star = i
                j += 1
            elif j < n and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1
            elif star != -1:
                i_star += 1
                i = i_star
                j = star + 1
                """
                s = abcde
                p = a*de
                """
            else:
                return False

        # handle the rest patterns
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
