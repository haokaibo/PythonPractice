# lambda arguments: expression
add10 = lambda x: x + 10
print(add10(5))

mult = lambda x, y: x * y
print(mult(2, 7))

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)
points2D_sorted_by_y = sorted(points2D, key=lambda p: p[1])
print(f'points2D={points2D}\npoints2D_sorted={points2D_sorted}\n'
      f'points2D_sorted_by_y={points2D_sorted_by_y}')

# map(func, seq)

a = [1, 2, 3, 4, 5, 6]
b = map(lambda x: x * 2, a)
print(list(b))

# filter(func, seq)
d = filter(lambda x: x % 2 == 0, a)
print(list(d))

# list function
c = [x * 2 for x in a]
print(c)

e = [x for x in a if x % 2 == 0]
print(e)

# reduce(func, seq)
from functools import reduce

a = [1, 2, 3, 4]

product_a = reduce(lambda x, y: x * y, a)
print(product_a)
