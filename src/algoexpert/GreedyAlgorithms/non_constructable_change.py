"""
Non-constructible Change

You're given an array of positive integers representing the values of coins
that you have. Write a function that determines the smallest amount of
change that you can't construct using the values of the coins.

You can only use each value at most as many times as it appears in the
coins array.

If you can't construct any amount of change, the function should return 0.
"""

# Time complexity is nlog(n) + n**2 -> n**2
def nonConstructibleChange(coins):
    ## Solution
    # Edge case
    if coins is None or len(coins) == 0:
        return 1
    # Define a set to hold the combinations of the possible sums of the coins
    sorted_coins = sorted(coins)
    possible_sums = {0}
    count = 1
    
    for c in sorted_coins:
        temp_set = set()
        
        for s in possible_sums:
            if s + c in possible_sums:
                continue
            if s + c != count:
                return count
            temp_set.add(s + c)
            count += 1
            
        possible_sums.update(temp_set)
        
    return count

print(nonConstructibleChange( [5, 7, 1, 1, 2, 3, 22]))