# Solution
# Use the mem dict object as the cache of the fib(n), then optimize the time complexity from O(2^n) to O(n)
# The space complexity is still O(n)
def fib(n, mem=dict()):
    if n == 0:
        mem[n] = 0
    elif n == 1:
        mem[n] = 1
    else:
        if n not in mem:
            mem[n] = fib(n - 1, mem) + fib(n - 2, mem)

    return mem[n]

# n = 3
# fib(2, mem) + fib(3, mem)
# fib(1, mem) + fib(0), mem) -> mem[0] = 0, mem[1] = 1
# mem[2] = 0 + 1 = 1
# fib(2, mem) + fib(1, mem) -> mem[2]+ mem[1] = 2
# mem[3] = 2

def getNthFib(n):
    # Write your code here.
    return fib(n - 1)
