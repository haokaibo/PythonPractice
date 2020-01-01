'''
In the first step, we divide the list into two sublists.  (Divide)

Then in the next step, we recursively sort the sublists in the previous step.  (Conquer)

Finally we merge the sorted sublists in the above step repeatedly to obtain the final list of sorted elements.  (Combine)

The recursion in step (2) would reach the base case where the input list is either empty or contains a single element (see the nodes in blue from the above figure).

Now, we have reduced the problem down to a merge problem, which is much simpler to solve. Merging two sorted lists can be done in linear time complexity {O(N)}O(N), where {N}N is the total lengths of the two lists to merge.
'''

class MergeSort:

    def merge_sort(nums):
        # bottom cases: empty or list of a single element.
        if len(nums) <= 1:
            return nums

        pivot = int(len(nums) / 2)
        left_list = MergeSort.merge_sort(nums[0:pivot])
        right_list = MergeSort.merge_sort(nums[pivot:])
        return MergeSort.merge(left_list, right_list)

    def merge(left_list, right_list):
        left_cursor = right_cursor = 0
        ret = []
        while left_cursor < len(left_list) and right_cursor < len(right_list):
            if left_list[left_cursor] < right_list[right_cursor]:
                ret.append(left_list[left_cursor])
                left_cursor += 1
            else:
                ret.append(right_list[right_cursor])
                right_cursor += 1

        # append what is remained in either of the lists
        ret.extend(left_list[left_cursor:])
        ret.extend(right_list[right_cursor:])

        return ret
