# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
from itertools import product

a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(f'prod of {a} and {b} is {list(prod)}')
c = [3]
prod = product(a, c, repeat=2)
print(f'twice prod of {a} and {c} is {list(prod)}')

from itertools import permutations

a = [1, 2, 3]
perm = permutations(a)
print(f'permutations of {a} is {list(perm)}')

perm = permutations(a, 2)
print(f'Repeat 2 permutations of {a} is {list(perm)}')

from itertools import combinations

a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(f'combinations of {a} is {list(comb)}')

from itertools import combinations_with_replacement

a = [1, 2, 3, 4]
comb = combinations_with_replacement(a, 2)
print(f'combinations_with_replacement of {a} is {list(comb)}')

from itertools import accumulate

a = [1, 2, 5, 3, 4]
acc = accumulate(a)
print(f'accumulate of {a} is {list(acc)}.')
print(f'accumulate(func=max) of {a} is {list(accumulate(a, func=max))}')
import operator

print(f'accumulate(func=operator.mul) of {a} is {list(accumulate(a, func=operator.mul))}')

from itertools import groupby

a = [1, 2, 3, 4]


def smaller_than_3(x):
    return x < 3


group_obj = groupby(a, key=smaller_than_3)
print(f'groupby smaller_than_3 for {a}.')
for key, value in group_obj:
    print(key, list(value))

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, {'name': 'Lisa', 'age': 27},
           {'name': 'Claire', 'age': 28}]
group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))

from itertools import count, cycle, repeat
for i in count(10,5):
    print(i)
    if i==15:
        break

a = [1,2,3]
index = 0
for i in cycle(a):
    print(i)
    index+=1
    if index == 10:
        break

for i in repeat(2, 3):
    print(i)
    index+=1
