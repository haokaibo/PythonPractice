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


if __name__ == '__main__':
    # StringHelper().print_reversed_string('abc')
    string = ['a', 'b', 'c']
    StringHelper().reverseString(string)
    print(string)
