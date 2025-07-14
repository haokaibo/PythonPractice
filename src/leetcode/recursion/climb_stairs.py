class ClimbStairs:
    def climbStairs(self, N):
        cache = {}
        if N == 0:
            return 0

        def recur_climb_stairs(N):
            if N in cache:
                return cache[N]

            if N == 1:
                cache[N] = 1
            elif N == 2:
                cache[N] = 2
            else:
                cache[N] = recur_climb_stairs(N - 1) + recur_climb_stairs(N - 2)
            return cache[N]

        return recur_climb_stairs(N)


if __name__ == '__main__':
    print(ClimbStairs().climbStairs(10))
