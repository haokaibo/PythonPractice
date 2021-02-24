'''
   a b c d e
h1 1 2 3 4 1
h2 2 3 4 5 1
h3 1 2 2 3 7

Sketch
   0 1 2 3 ...
h1 1 2 3 4
h2 4 3 2 1
h3 1 0 1 3
'''


class HashFunction:
    def __init__(self, prime, odd, limit):
        self.prime = prime
        self.odd = odd
        self.limit = limit

    def get_hash_val(self, character):
        hash_code = abs(hash(character))
        return self.calculate_hash(hash_code, self.prime, self.odd)

    def calculate_hash(self, hash_code, prime, odd):
        return ((((hash_code % self.limit) * prime) % self.limit) * odd) % self.limit


class Solution:
    def __init__(self, cols=1000000000, rows=4):
        self.sketch = [[0 for _ in range(cols)] for _ in range(rows)]
        self.hash_funcs = []
        # for r in range(rows):
        #     hash_funcs.append()
        h1 = HashFunction(11, 9, cols)
        h2 = HashFunction(17, 15, cols)
        h3 = HashFunction(31, 29, cols)
        h4 = HashFunction(61, 39, cols)
        self.hash_funcs.extend((h1, h2, h3, h4))

    def increase_value(self, character):
        for index, func in enumerate(self.hash_funcs):
            self.sketch[index][func.get_hash_val(character)] += 1

    def get_amount(self, character):
        min_amount = self.sketch[0][self.hash_funcs[0].get_hash_val(character)]
        for i in range(1, len(self.sketch)):
            min_amount = min(min_amount, self.sketch[i][self.hash_funcs[i].get_hash_val(character)])

        return min_amount


s = Solution()
chars = ['a', 'b', 'c', 'd', 'e']
counters = {}
for i in range(100):
    for c in chars:
        if c not in counters:
            counters[c] = 0
        counters[c] += 1
        s.increase_value(c)
for i in range(10):
    counters['c'] += 1
    s.increase_value('c')

print("\n".join([str(i) for i in s.sketch]))

print(f"counters={counters}")
for c in chars:
    print(c, s.get_amount(c))
