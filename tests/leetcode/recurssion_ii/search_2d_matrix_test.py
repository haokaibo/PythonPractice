from unittest import TestCase

from leetcode.recursion_ii.search_2d_matrix import Search2DMatrix


class Search2dMatrixTest(TestCase):
    def test_searchMatrix1(self):
        assert not Search2DMatrix().searchMatrix(
            [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
            , 20)

    def test_searchMatrix2(self):
        assert Search2DMatrix().searchMatrix(
            [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
            , 5)

    def test_searchMatrix3(self):
        assert Search2DMatrix().searchMatrix(
            [[-1, 3]],
            3)

    def test_searchMatrix3(self):
        assert Search2DMatrix().searchMatrix(
            [[1], [2], [3], [4], [5]],
            2)

    def test_searchMatrix4(self):
        assert Search2DMatrix().searchMatrix(
            [[1], [2], [3], [4], [5]],
            5
        )

    def test_searchMatrix5(self):
        assert not Search2DMatrix().searchMatrix(
            [[1, 1]],
            2
        )

    def test_searchMatrix6(self):
        assert Search2DMatrix().searchMatrix(
            [[-5]],
            -5
        )

    def test_searchMatrix7(self):
        assert not Search2DMatrix().searchMatrix(
            [[-1], [-1]],
            0
        )

    def test_searchMatrix8(self):
        assert not Search2DMatrix().searchMatrix(
            [[1, 4], [2, 5]]
            , 3
        )
