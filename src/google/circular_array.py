not_circular_array = [1, 2, 3, 4, 5, 6]
circular_array = [1, 2, 1, 4, 5, 6]


def check_circular_array(arr):
    '''
    Time complexity is O(n).
    :param arr:
    :return:
    '''
    if arr is None:
        return False

    p = q = 0
    arr_len = len(arr)

    if arr_len <= 1:
        return False

    while True:
        if 0 <= p < arr_len and 0 <= q < arr_len:
            p = arr[p]
            if 0 <= p < arr_len:
                if p == q:
                    return True
                else:
                    p = arr[p]
                    if 0 <= p < arr_len:
                        if p == q:
                            return True
                        else:
                            q = arr[q]
                            if p == q:
                                return True
                    else:
                        return False
            else:
                return False
        else:
            return False


print(check_circular_array(not_circular_array))
print(check_circular_array(circular_array))
