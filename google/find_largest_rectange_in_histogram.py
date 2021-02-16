"""
Given an array which represent the x coordinates for a histogram chart,
find the largest area in the histogram.
"""

arr = [1, 2, 3, 4, 5, 2, 3, 2]


def find_largest_area_in_histogram(arr):
    max_area = 0
    if arr is None or len(arr) == 0:
        return max_area

    num_dic = dict()
    for i, v in enumerate(arr):
        if v not in num_dic:
            num_dic[v] = i
            max_area = max(v, max_area)
        else:
            # check all the previous bars are greater and equals to me
            all_greater_or_equals_to_me = True
            for j in range(num_dic[v] + 1, i):
                if arr[j] < v:
                    all_greater_or_equals_to_me = False
                    break

            if all_greater_or_equals_to_me:
                max_area = max((i - num_dic[v] + 1) * v, max_area)

    return max_area


print(find_largest_area_in_histogram(arr))
