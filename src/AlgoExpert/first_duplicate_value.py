def firstDuplicateValue(array):
    # Write your code here.
    """
    Solution(Time: O(n), Space: O(n))
    1. Use a set to hold the unique numbers in the array. 
    2. Iterate the array, if there is any element apprears the second time in the set just return number.
    """

    uniques = set()
    for num in array:
        if num not in uniques:
            uniques.add(num)
        else:
            return num
    
    return -1


def optimized_firstDuplicateValue(array):
    """
    Solution(Time: O(n), Space: O(1))
    0: Since the number is 1 to n, all are greater than 0, and n is the length of the array
    1. Use the index as the flag of the number's existence. e.g. [1, 5, 1] , 
    when read the number 1 at index 0, we just calculate the flag index with
    flagIndex = abs(currentNumberIndex - 1) = abs(0 - 1) = 5, 
    then flag it by set the array[flagIndex] = array[flagIndex] * -1
    2. We calculate each number in the array, while when we found a calculation result of a 
    number in the array is already negative. just return it, due to we have already found a duplicate one below.
    """

    for i in range(len(array)):
        flagIndex = abs(array[i]) - 1
        if array[flagIndex] < 0:
            return abs(array[i])
        else:
            array[flagIndex] *= -1 
    
    return -1

print(optimized_firstDuplicateValue([2, 1, 5, 2, 3, 3, 4]))