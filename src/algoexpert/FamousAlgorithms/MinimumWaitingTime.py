def minimumWaitingTime(queries):
    # Write your code here.
    # Solution
    # Time complexity: O(n Log(n) + n)=> O()nlog(n))
    # Space complexity: O(n)
    # sort the array queries
    queries.sort()

    # iterate the sorted array and calculate the sum, the trick is calculate the 
    # previous sum multiply 2 then plug current value
    # The last element will not be calculated.

    waiting_time = 0
    previous_sum = 0
    for i in range(1, len(queries)):
        current_sum = previous_sum + queries[i - 1]
        waiting_time += current_sum
        previous_sum = current_sum
    return waiting_time


# Thinking
# [3, 2, 1]

# waiting time: 
# [3, 2, 1, 2, 6] 
# (0) + (3) + (3 + 2) + (3 + 2 + 1) + (3 + 2 + 1 + 2 ) = 22
# The minimum is 17 which is given
# The possible order would be:
# [1, 2, 2, 3, 6]
# (0) + (1) + (1+2) + (1+ 2 + 2) + (1 + 2 + 2 + 3) = 17
    
# The optimized order should be a sorted array in ascendant order
