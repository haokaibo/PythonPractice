"""
0 1 1 0
1 1 1 0
1 1 1 0
0 0 0 0

the max ones matrix is 2X2

1 1
1 1
"""

matrix = [[1, 1, 1, 0, 0, 0],
          [1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1],
          [0, 1, 1, 1, 1, 1],
          [0, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0]]


def get_max_ones_matrix_num(matrix):
    '''
    Time complexity is O(n)
    :param matrix:
    :return:
    '''
    max_num = 0
    rows = len(matrix)
    cols = len(matrix[0])

    if matrix is None or rows == 0 or cols == 0:
        return max_num

    # build a cache to store the iteration result
    cache = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if i == 0 or j == 0 or matrix[i][j] == 0:
                cache[i][j] = matrix[i][j]
            else:
                cache[i][j] = min(cache[i - 1][j], cache[i - 1][j - 1], cache[i][j - 1]) + matrix[i][j]
            max_num = max(cache[i][j], max_num)

    print('\n'.join(str(c) for c in cache))

    return max_num


print(get_max_ones_matrix_num(matrix))
