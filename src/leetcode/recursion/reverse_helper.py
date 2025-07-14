from typing import List


class StringHelper:
    def print_reversed_string(self, str):
        self.reverse_print(0, str)

    def reverse_print(self, index, str):
        if index == len(str):
            return
        self.reverse_print(index + 1, str)
        print(str[index])

    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)

    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        _reversed = list(s)

        left = 0
        right = len(_reversed) - 1

        while left < right:
            while left < right and _reversed[left].lower() not in vowels:
                left += 1
            while left < right and _reversed[right].lower() not in vowels:
                right -= 1
            if left < right:
                _reversed[left], _reversed[right] = _reversed[right], _reversed[left]
                left += 1
                right -= 1

        return ''.join(_reversed)


if __name__ == '__main__':
    # test 1
    # StringHelper().print_reversed_string('abc')

    # test 2
    # string = ['a', 'b', 'c']
    # StringHelper().reverseString(string)
    # print(string)

    # test 3
    # print(StringHelper().reverseVowels('hello'))
    with open('test.txt') as f:
        string = f.read()
        result = StringHelper().reverseVowels(string)
        print(result)
