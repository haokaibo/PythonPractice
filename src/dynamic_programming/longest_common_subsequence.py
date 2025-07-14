"""
Given two strings, find the max count of common subsequent characters in the two strings.
e.g
a:d[ab]c[e]
b:[ab]d[e]
most_common subsequence = abe
I: str_a, str_b
O: number_of_max_count_of_common_characters
"""


class LCS:
    def __init__(self):
        self.dic = dict()
        self.longest_common_characters = []

    def get_longest_common_sequence(self):
        return "".join(self.longest_common_characters)

    def lcs(self, p, q, m, n):
        result = (0, None)
        if (m, n) in self.dic:
            return self.dic[(m, n)]
        if m > len(p):
            raise ValueError(f"parameter m={m} should be less or equals to the length of p.len={len(p)}.")
        if n > len(q):
            raise ValueError(f"parameter n={n} should be less or equals to the length of q.len={len(q)}.")
        if n == 0 or m == 0:
            result = (0, '')
        elif p[m - 1] == q[n - 1]:
            temp = self.lcs(p, q, m - 1, n - 1)
            result = (1 + temp[0], f'{temp[1]}{p[m - 1]}')
        elif p[m - 1] != q[n - 1]:
            max1 = self.lcs(p, q, m - 1, n)
            max2 = self.lcs(p, q, m, n - 1)
            result = max(max1, max2, key=lambda item: item[0])
        self.dic[(m, n)] = result

        return result


a_str = "dabfce"
b_str = "abfde"
app = LCS()
result = app.lcs(a_str, b_str, len(a_str), len(b_str))
print(result)
# print(app.get_longest_common_sequence())

# try to raise an error
# print(lcs(a_str, b_str, 10, 10))
