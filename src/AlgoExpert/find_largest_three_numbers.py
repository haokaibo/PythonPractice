def findThreeLargestNumbers(array):
    # Write your code here.
    # Solution
    # Use a new array to hold the largest 3 numbers in ascending order. e.g. [1, 2, 3]
    # Time complexity: O(n)
    # Space complexity: O(1)
    N = 3
    largest_n = [None] * N
    # Iterate the array, 
    for n in array:
        index = 0
        while index < N and (largest_n[index] is None or n > largest_n[index]):
            index += 1
        # if a number is larger than any element in the array, insert the number into the array. and pop the first element in the array.
        if index > 0:
            largest_n.insert(index, n)
            largest_n.pop(0)
            
    return largest_n

if __name__ == "__main__":
    print(findThreeLargestNumbers([1, 2, 3]))
