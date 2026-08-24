def bestSeat(seats):
    # Write your code here.
    """
    Solution (Time: O(n), Space: O(1))
    e.g. 
    [1, 0, 1] -> 1
    [1, 0, 0, 1] -> 1
    [1, 0, 0, 0, 1] -> 2
    [1, 0, 1, 0, 0, 0, 1] -> 4
    [1, 1, 0, 1]
    1. Find the consecutive zeros in the array between ones.
    2. Prioritize space size(length of the consecutive zeros) in the array for the best seat
    """
    # variables to hold the pointer which points to one
    previous_one = 0

    # current pointer
    current = 1

    # max space to hold the best space we can get for current iteration
    max_space = 0

    best_seat = -1

    """
    [1, 0, 0, 1, 0, 0, 1]
    current_space = 3 - 0 - 1 > max_space 
    max_space = 2
    best_seat = (3 - 0) // 2 = 1
    previous_one = current = 3
    ---
    current = 6
    current_space = 6 - 0 - 3 not > max_space 
    max_space = 3
    best_seat = 1
    previous_one = current = 6
    current = 7
    """
    while current < len(seats):
        while current < len(seats) and seats[current] == 0:
            current += 1

        current_space = current - previous_one - 1
        if current_space > max_space:
            max_space = current_space
            best_seat = (current + previous_one) // 2

        previous_one = current
        current += 1

    return best_seat

def optimized_bestSeat(seats):
    best = -1
    zero = start = length = 0
    for i, num in enumerate(seats):
        if num == 0:
            zero += 1
        else:
            if zero > length:
                best, length = (i + start) // 2, zero
            zero, start = 0, i
    return best