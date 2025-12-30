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
        current = 0
        for j in range(array_length - i):
            if array[current] > array[j]:
                temp = array[j]
                array[j] = array[current]
                array[current] = temp

            current = j
            

    return array
if __name__ == "__main__":
    print(bubbleSort([8,5,2,9,5,6,3]))