'''
I: [2,1,6,9,4,3]
O: 4 -> [1,2,3,4]
Solution:
Feed all the input element in the array to a dict.
Iterate the dict to find the longest path by increment by 1.
Cache the length to the dict value for each key.
'''


class Solution:
    def __init__(self):
        self.d = {}

    def get_next_length(self, k):
        if k not in self.d:
            return 0
        elif self.d[k] == 0:  # not cached
            return 1 + self.get_next_length(k + 1)
        else:
            return self.d[k]

    def find_longest_subs(self, arr):
        if arr is None or len(arr) == 0:
            return None

        for i in arr:
            self.d[i] = 0

        longest_length_head = None
        longest_length = 0
        for k, v in self.d.items():
            self.d[k] = 1 + self.get_next_length(k + 1)
            if longest_length < self.d[k]:
                longest_length = self.d[k]
                longest_length_head = k

        return [i for i in range(longest_length_head, longest_length_head + longest_length)]


s = Solution()
print(s.find_longest_subs([2, 1, 6, 9, 4, 3]))
