# Sets: unordered, mutable, no duplicates
set1 = {1, 2, 3}
set1.add(1)
print(set1)

# sort
set2 = set('hello')
print(sorted(set2))

# pop
print(set2)
print(set2.pop())
print(set2)

# union
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

# intersection
i=evens.intersection(primes)
print(i)

# difference
set_a={1,2,3,4,5,6,7,8,9}
set_b={1,2,3,10,11,12}

diff = set_a.difference(set_b)
print(diff)

# symmetric_difference
symmetric_diff = set_a.symmetric_difference(set_b)
print(symmetric_diff)

# update
set_a.update(set_b)
print(f'update={set_a}, set_b={set_b}')

# intersection update
set_a={1,2,3,4,5,6,7,8,9}
intersection_update = set_a.intersection_update(set_b)
print(f'set_a={set_a}')

# difference update
set_a={1,2,3,4,5,6,7,8,9}
set_a.difference_update(set_b)
print(f'set_a={set_a}')

# symmetric difference
set_a={1,2,3,4,5,6,7,8,9}
set_a.symmetric_difference_update((set_b))
print(f'set_a={set_a}')

# issubset
set_a={1,2,3,4,5,6}
set_b={1,2,3}
set_c={7,8}
print(f"set_b is subset of set_a: {set_b.issubset(set_a)}")
print(f"set_a is superset of seb_b: {set_a.issuperset(set_b)}")
print(f"set_a is disjoint set of set_c: {set_a.isdisjoint(set_c)}")

# frozenset
f_set = frozenset([1,2,3,4])

print(f'f_set={f_set}')
print(f'set_a={set_a}')