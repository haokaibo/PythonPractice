"""
Min Number Of Coins For Change

You're given an integer "targetAmount" and an array of distinct coins. Write
a function that calculates the minimum number of coins needed to make a
total amount of "targetAmount". If it's impossible to make the target amount,
the function should return -1.

You can assume that all coin values are positive integers, and that there is
at least one coin.
"""

"""
Solution(Time: O(n * d),Space: O(n))
Target: Use lease amount of coins for the change
1. impossible, return -1
2. n == 0, return 0
3. n >= 1, 
Basic idea: we can use a list to store the minimum coins for every amount up to n, 
and we can update this list iteratively for each denomination. The minimum coins needed for each amount is 
the minimum of the 2 below:
1. The value in the remaining corresponding to the amount in the list plus one (to use the current denomination).
2. The value in the current amount position of the list
"""

class Solution:
    @staticmethod
    def minNumberOfCoinsForChange(n, denoms):
        # Create an array to store the minimum coins for every amount up to n
        num_of_coins = [float('inf')] * (n + 1)
        num_of_coins[0] = 0 # 0 coins needed to make amount 0
        
        for denom in denoms:
            
            for amount in range(denom, n + 1):
                # We update the current amount if using the current coin is better
                # print(f"denom: {denom}, amount: {amount}, num_of_coins[{amount}]: {num_of_coins[amount]}, num_of_coins[{amount - denom}] + 1: {num_of_coins[amount - denom] + 1}")
                num_of_coins[amount] = min(num_of_coins[amount], num_of_coins[amount - denom] + 1)
                # print(f"num_of_coins[{amount}]: {num_of_coins[amount]}, num_of_coins: {num_of_coins}")

        return num_of_coins[n] if num_of_coins[n] != float('inf') else -1


print(f"{Solution.minNumberOfCoinsForChange(7, [1, 2, 5])}")
