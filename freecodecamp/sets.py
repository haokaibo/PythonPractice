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

i=evens.intersection(primes)
print(i)