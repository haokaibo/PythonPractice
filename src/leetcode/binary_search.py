from typing import List


class BinarySearch:
    def binary_search(self, nums: List[int], target: int, left: int, right: int):
        if nums is None or len(nums) == 0 or left > right:
            return -1
        else:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return self.binary_search(nums, target, left, mid-1)
            else:
                return self.binary_search(nums, target, mid+1, right)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums)-1)


if __name__ == '__main__':
    bs = BinarySearch()
    print(bs.search([1,2,3], 3))