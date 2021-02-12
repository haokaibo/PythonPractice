"""
- The difference between arguments and parameters
- Positional and keyword arguments
- Default arguments
- Variable-length arguments (*args and **kwargs)
- Container unpacking into function arguments
- Local vs. global arguments
- Parameter passing (by value or by reference?)
"""
from typing import List

# - Positional and keyword arguments
# - Default arguments
def foo(a, b, c=4):
    print(a, b, c)


foo(b=1, a=2)

# - Variable-length arguments (*args and **kwargs)
def foo2(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])


foo2(1, 2, 3, four=4, five=5)

# - Container unpacking into function arguments
def foo3(a, b, *, c, d):
    print(a, b, c, d)


foo3(1, 2, c=3, d=4)


def foo4(*args, last):
    for arg in args:
        print(arg)
    print(last)


foo4(1, 2, 3, last=4)


# - Container unpacking into function arguments
def foo5(a, b, c):
    print(a, b, c)


foo5(*[1, 2, 3])
foo5(**{'a': 1, 'b': 2, 'c': 3})


# - Local vs. global arguments
def foo6():
    global number
    number = 3
    x = number
    print(f'number inside function: {x}.')


foo6()


def foo7():
    global number
    number += 1
    print(f'number inside function: {number}.')

foo7()


# - Parameter passing (by value or by reference?)
def foo8(x, y: List[int]):
    x = 5
    y.append(4)


immutable_var = 10
mutable_list: List[int] = [1, 2, 3]
foo8(immutable_var, mutable_list)
print(f'immutable_var={immutable_var}, mutable_list={mutable_list}')
