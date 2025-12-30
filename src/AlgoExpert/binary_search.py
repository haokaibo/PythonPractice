# Time complexity O(log(n))
# Space complexity O(1)
def binary_search(array, target):
    begin = 0
    end = len(array) - 1
    while begin <= end:
        mid = (begin + end) // 2
        mid_value = array[mid]
        if mid_value == target:
            return mid
        elif mid_value < target:
            begin = mid + 1
        else:
            end = mid - 1

    return -1
    
def binarySearch(array, target):
    # Write your code here.
    return binary_search(array, target)


