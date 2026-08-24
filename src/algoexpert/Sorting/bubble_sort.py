"""
Bubble Sort

Write a function that takes in an array of integers and sorts the array in
place using the Bubble Sort algorithm, and then returns it.

If the input array is empty, the function should simply return it.

The Bubble Sort algorithm works by first iterating through the array from
left to right, comparing each element to its right neighbor. If the element
is greater than its right neighbor, the two elements are swapped. This
process continues until the end of the array, where the biggest element
"bubbles" to the end of the array. This process repeats, with each pass
"bubbling" the next biggest element to its proper position, until the array
is sorted.
"""

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