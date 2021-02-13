from abc import ABC, abstractmethod


class AbstractClassExample(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def do_something(self):
        print('Super class implementation on do_something.')

    def __str__(self):
        return str(self.value)


class SubClass(AbstractClassExample):

    def do_something(self):
        super().do_something()
        print("Sub class's implementation on do_something.")
        return self.value + 1


sub = SubClass(1)
print(sub.do_something())