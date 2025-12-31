def bubbleSort(array):
    # Write your code here.
    # Solution
    # Bubble sort is an iterative process that iterates through the array, 
    # compares the elements with the remaining elements, and if it finds the right position, swaps the two numbers.
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    array_length = len(array)

    # [30, 10, 2] -> [10, 30, 2]
    # 
    # [10, 2, 30]
    
    for i in range(array_length):
        for j in range(1, array_length-i):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]

    return array
    
if __name__ == "__main__":
    print(bubbleSort([2, 3, 5, 5, 6, 8, 9]))