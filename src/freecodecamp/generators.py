import sys


def generator1():
    yield 1
    yield 2
    yield 3


g = generator1()

value = next(g)
print(value)

for i in g:
    print(i)


# sorted(g)

def count_down(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1


cd = count_down(4)
for _ in range(4):
    print(next(cd))


def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(sys.getsizeof(firstn_generator(1000000)))
print(sum(firstn_generator(1000000)))


def fibonacci(limit):
    # 0 1 1 2 3 5 8 13 ...
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonacci(20)
for i in fib:
    print(i)

generator2 = (i for i in range(10000) if i % 2 == 0)

list2 = [i for i in range(10000) if i % 2 == 0]

print(f'list(generator2)={list(generator2)}\nThe size of it is {sys.getsizeof(generator2)}.')
print(f'list2={list2}\nThe size of it is {sys.getsizeof(list2)}.')

