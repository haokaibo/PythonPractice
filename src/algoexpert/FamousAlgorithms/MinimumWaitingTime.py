"""
Minimum Waiting Time

You're given an array of positive integers representing the durations of
requests. The ith integer represents the duration of the ith request. The
requests must be processed in the order they are received (no re-ordering),
and only one request can be processed at a time.

Write a function that returns the minimum total wait time as if no requests
have been processed yet. For example, if durations = [1, 2, 3, 4], the total
wait time is 10:

* Request 1 takes 0 to process (since it's the first request) and has a wait
  time of 0
* Request 2 takes 1 to process (after the first request completes) and has a
  wait time of 1
* Request 3 takes 3 to process and has a wait time of 1 + 2 = 3
* Request 4 takes 6 to process and has a wait time of 1 + 2 + 3 = 6

This is a total wait time of 0 + 1 + 3 + 6 = 10.
"""

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
