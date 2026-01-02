def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    smallest_gap = float('inf')
    current_gap = float('inf')

    smallest_gap_pair = []

    # O(log(n) + log(m))
    arrayOne.sort()
    arrayTwo.sort()

    p1 = 0
    p2 = 0

    while p1 < len(arrayOne) and p2 < len(arrayTwo):
        n1 = arrayOne[p1]
        n2 = arrayTwo[p2]
        if n1 == n2:
            return [n1, n2]
        elif n1 < n2:
            current_gap = n2 - n1
            p1 += 1
        else:
            current_gap = n1 - n2
            p2 += 1

        if current_gap < smallest_gap:
            smallest_gap = current_gap
            smallest_gap_pair = [n1, n2]

    return smallest_gap_pair


print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))