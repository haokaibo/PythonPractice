from typing import List

'''Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?'''

class PascalTriangle2:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        if rowIndex < 1:
            return result

        def helper(parent: List[int]):
            begin = 0
            parent_len = len(parent)
            end = parent_len
            parent.append(0)
            previous = 0
            while begin <= parent_len / 2:
                value = 0
                if begin > 0:
                    value = parent[begin] + previous
                else:
                    value = parent[begin]
                previous = parent[begin]
                parent[begin] = value
                parent[end] = value
                begin += 1
                end -= 1
            return parent

        for i in range(rowIndex):
            helper(result)
        return result


if __name__ == '__main__':
    print(PascalTriangle2().getRow(3))
