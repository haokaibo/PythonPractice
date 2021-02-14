'''
You are given an array of repeating numbers.
All numbers repeat in an even way, except for one. Find that odd occurring number.
'''

repeat_numbers = [1, 1, 4, 2, 2, 3, 3, 3, 4]


# The expected output is 3

def find_occurring_number(arr):
    '''
    The time complexity of this is O(n).
    :param arr:
    :return:
    '''
    if arr is None:
        return None
    num_set = set()
    for num in arr:
        if num in num_set:
            num_set.remove(num)
        else:
            num_set.add(num)
    if len(num_set) == 0:
        return None
    else:
        return num_set.pop()


print(find_occurring_number(repeat_numbers))
