class Pow:

    def myPow(self, x: float, n: int) -> float:
        cache = {}

        def helper(x: float, n: int) -> float:
            if x == 0:
                return 0.0
            if n == 0:
                return 1
            elif n == 1:
                return x;
            elif n > 1:
                if n in cache:
                    return cache[n]
                elif n % 2 == 0:
                    cache[n] = helper(x, n / 2) * helper(x, n / 2)
                else:
                    cache[n] = helper(x, (n - 1)) * x
                return cache[n]
            elif n == -1:
                return 1.0 / x
            elif n < -1:
                if n in cache:
                    return cache[n]
                elif n % 2 == 0:
                    cache[n] = helper(x, n / 2) * helper(x, n / 2)
                else:
                    cache[n] = helper(x, (n + 1)) * 1.0 / x
                return cache[n]

        return helper(x, n)

if __name__=='__main__':
    assert 0.25 == Pow().myPow(2,-2)