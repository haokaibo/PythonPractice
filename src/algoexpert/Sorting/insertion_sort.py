def insertionSort(array):
    # Write your code here.
    # Solution
    # Iterate the array, for each iterated item, find the proper position for it.
    # since the elements before that element is sorted already, we just need to find the right position for it.
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1 
        
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j+1] = key
        
    
    return array


if __name__ == "__main__":
    print(insertionSort([2, 3, 1]))