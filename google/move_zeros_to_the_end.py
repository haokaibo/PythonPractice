'''
Move all zeros present in the array to the end and return the same array
'''


def find_next_non_zero_index(begin, arr):
    for i in range(begin, len(arr)):
        if arr[i] != 0:
            return i
    return -1


def move_zeros_to_end(arr):
    if arr is None or len(arr) == 0:
        return arr

    arr_len = len(arr)
    index = 0
    for i in range(arr_len):
        if arr[i] != 0:
            index += 1
            continue
        else:
            index = find_next_non_zero_index(index + 1, arr)
            if index == -1:
                break
            arr[i], arr[index] = arr[index], arr[i]
    return arr


origin_arr = [1, 2, 3, 0, 1, 0, 0, 1, 2, 3, 3]
print(f'{origin_arr}\n{move_zeros_to_end(origin_arr)}')
print(move_zeros_to_end([1]))
print(move_zeros_to_end([1, 0, 1]))
print(move_zeros_to_end([1, 0, 0]))
print(move_zeros_to_end([1, 0, 0, 1, 1, 1, 1, 0]))
