"""
Given a number N which will form a fibonacci array, find number x in the
0, 1, 1, 2, 3, 5, 8, 13, 21, ...
"""

cache = {}


def fibonacci_with_cache(pos):
    if pos == 0 or pos == 1:
        cache[pos] = pos
        return cache[pos]
    else:
        if pos not in cache:
            cache[pos] = fibonacci_with_cache(pos - 1) + fibonacci_with_cache(pos - 2)
        return cache[pos]


print(fibonacci_with_cache(7))


def fibonacci_with_constant_space(pos):
    if pos == 0 or pos == 1:
        return pos
    else:
        sec_last = 0
        last = 1
        curr_pos = 2
        while curr_pos <= pos:
            last, sec_last = last + sec_last, last
            curr_pos += 1
        return last


print(fibonacci_with_constant_space(7))
