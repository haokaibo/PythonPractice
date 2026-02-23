def optimizedNumberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    """Solution (Time: O(n^2), Space: O(n))
    1. Build an array to hold the for each value of the possible ways count for each number from 0 to n.
    2. Use the denoms one by one to find the possible ways.
    3. The formula whould be ways[n] = ways[n] + ways[n - denom]
    """
    nums = [0 for _ in range(n + 1)]
    nums[0] = 1 # There is always a way to find the change for the situation that n == 0

    for denom in denoms:
        if denom > n:
            continue

        for i in range(denom, n + 1):
            nums[i] += nums[i - denom]

    return nums[n]