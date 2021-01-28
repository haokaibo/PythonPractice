class Search2DMatrix:
    def searchArray(self, array, target):
        if array is None or len(array) == 0:
            return False
        mid = (len(array) - 1) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            return self.searchArray(array[:mid], target)
        else:
            return self.searchArray(array[mid + 1:], target)

    def searchVerticalArray(self, matrix, target):
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        mid = (len(matrix) - 1) // 2
        if matrix[mid][0] == target:
            return True
        elif matrix[mid][0] > target:
            return self.searchVerticalArray(matrix[:mid], target)
        else:
            return self.searchVerticalArray(matrix[mid + 1:], target)

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if None is matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        m = len(matrix)
        n = len(matrix[0])

        # if it is just one dimension just search the array.
        if m == 1:
            return self.searchArray(matrix[0], target)
        if n == 1:
            return self.searchVerticalArray(matrix, target)

        row_mid = (m - 1) // 2
        col_mid = (n - 1) // 2

        # print(f'matrix: {matrix}, row_mid: {row_mid}, col_mid: {col_mid}')
        mid_val = matrix[row_mid][col_mid]

        if target == mid_val:
            return True
        elif m == 1 and n == 1:
            return False
        elif target < mid_val:
            row_up = max(0, row_mid - 1)
            mid_up_val = matrix[row_up][col_mid]
            if target == mid_up_val:
                return True
            elif target < mid_up_val:
                return self.searchMatrix([matrix[i][:col_mid + 1] for i in range(row_mid + 1)], target)
            elif target > mid_up_val:
                if self.searchMatrix([matrix[i][col_mid + 1:] for i in range(row_mid)], target):
                    return True
                if self.searchMatrix([matrix[i][:col_mid] for i in range(row_mid, m)], target):
                    return True

        elif target > mid_val:
            row_down = min(row_mid + 1, m - 1)
            mid_down_val = matrix[row_down][col_mid]
            if target == mid_down_val:
                return True
            elif target < mid_down_val:
                if self.searchMatrix([matrix[i][:col_mid] for i in range(row_down, m - 1)], target):
                    return True
                if self.searchMatrix([matrix[i][col_mid + 1:] for i in range(row_mid)], target):
                    return True
            elif target > mid_down_val:
                col_index = col_mid
                if row_down == m - 1:
                    col_index = col_mid + 1
                return self.searchMatrix([matrix[i][col_index:] for i in range(row_mid, m)], target)

        return False


if __name__ == '__main__':
    assert not Search2DMatrix().searchMatrix(
        [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
        , 20)
