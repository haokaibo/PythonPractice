class StringHelper:
    def print_reversed_string(self, str):
        self.reverse_print(0, str)

    def reverse_print(self, index, str):
        if index == len(str):
            return
        self.reverse_print(index + 1, str)
        print(str[index])


if __name__ == '__main__':
    StringHelper().print_reversed_string('abc')
