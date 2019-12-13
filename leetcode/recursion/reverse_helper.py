from typing import List


class StringHelper:
    def print_reversed_string(self, str):
        self.reverse_print(0, str)

    def reverse_print(self, index, str):
        if index == len(str):
            return
        self.reverse_print(index + 1, str)
        print(str[index])

    def reverse_chars(self, chars: List[str]) -> None:
        self.reverse_chars_helper(chars, 0, len(chars)-1)

    def reverse_chars_helper(self, chars, begin, end):
        if begin >= end:
            return
        else:
            self.reverse_chars_helper(chars, begin + 1, end - 1)
            temp = chars[begin]
            chars[begin] = chars[end]
            chars[end] = temp


if __name__ == '__main__':
    # StringHelper().print_reversed_string('abc')
    string = ['a', 'b', 'c']
    StringHelper().reverse_chars(string)
    print(string)
