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
