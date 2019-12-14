from typing import List


class PascalTriangle:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return []

        def helper(parent: List[int]):
            child = [0]*(len(parent)+1)
            begin = 0
            parent_len = len(parent)
            end = parent_len
            while begin <= end:
                if begin > 0:
                    child[begin] = parent[begin - 1] + parent[begin]
                else:
                    child[begin] = parent[begin]
                if end == parent_len:
                    child[end] = parent[end - 1]
                else:
                    child[end] = parent[end - 1] + parent[end]
                begin += 1
                end -= 1
            return child

        parent = [1]
        result = [parent]
        for i in range(numRows-1):
            child = helper(parent)
            result.append(child)
            parent = child
        return result


if __name__ == '__main__':
    print(PascalTriangle().generate(1))
