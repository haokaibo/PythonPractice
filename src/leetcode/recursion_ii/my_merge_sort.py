from typing import List


class MyMergeSort:
    def sortArray(self, nums: List[int]) -> List[int]:
        if nums is None or len(nums) <= 1:
            return nums
        pivot = len(nums) // 2
        left = self.sortArray(nums[:pivot])
        right = self.sortArray(nums[pivot:])
        return self.merge(left, right)

    def merge(self, left: List[int], right: List[int]):
        left_index = right_index = 0
        result = []
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        # extend the left elements in the left or right arrays.
        result.extend(left[left_index:])
        result.extend(right[right_index:])
        return result


if __name__ == '__main__':
    sorter = MyMergeSort()
    result = sorter.sortArray([5, 2, 3, 1])
    assert [1,2,3,5] == result
