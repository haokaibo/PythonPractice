"""
Selection Sort

Write a function that takes in an array of integers and sorts the array in
place using the Selection Sort algorithm, and then returns it.

The Selection Sort algorithm works by finding the smallest integer in the
unsorted portion of the array, swapping it with the first unsorted integer,
and then moving the pointer one position to the right, repeating until the
array is sorted.
"""

def selectionSort(array):
    # Write your code here.
    # Solution
    # The selection sort is to iterate the array from i(start from 0) to n.
    # for each iteration, find the smallest/biggest element in the range(i+1, n), and then swap the smallest element with the element in the i position.
    # Time compelxity: O(n^2)
    # Space complexity: O(1)
    for i in range(len(array)):
        target = i
        for j in range(i+1, len(array)):
            if array[target] > array[j]:
                target = j
        array[i], array[target] = array[target], array[i]
        
    return array
