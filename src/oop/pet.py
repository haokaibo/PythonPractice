"""
Object oriented programming
- Inheritance
- Polymorphism
- Encapsulation
"""

from enum import Enum, unique


@unique
class Color(Enum):
    BLACK = 0
    WHITE = 1


class Pet:
    species = 'mammal'
    number_of_pets = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Pet.add_pet()

    @property
    def name(self):
        print('getting name..')
        return self._name

    @name.setter
    def name(self, name):
        print('setting name..')
        self._name = name

    @name.deleter
    def name(self):
        del self._name

    def __repr__(self):
        '''For debugging'''
        return f"Pet('{self.name}, {self.age}')"

    def __str__(self):
        return f'{self.name} who is {self.age} years old. I am from {Pet.species} species.'

    def __hash__(self):
        return hash(f"{self.name}{self.age}")

    def speak(self):
        return "I cannot speak."

    @classmethod
    def get_number_of_pets(cls):
        return cls.number_of_pets

    @classmethod
    def add_pet(cls):
        cls.number_of_pets += 1

    @staticmethod
    def do_nothing():
        pass


class Cat(Pet):
    def __init__(self, name, age, color: Color):
        super().__init__(name, age)
        self.color = color

    def __str__(self):
        return f'I am a Cat named {super().__str__()} And my color is {self.color.name}.'

    def speak(self):
        return "Meow"


class Dog(Pet):
    def __str__(self):
        return f'I am a Dog named {super().__str__()}'

    def speak(self):
        return "Wang"


missy = Cat('Missy', 3, Color.BLACK)
lucky = Dog('Lucky', 5)

print(f'missy.species={missy.species}')
print(f'Cat.species={Cat.species}')
print('\n'.join([missy.__str__(), lucky.__str__()]))


class Coffee(Cat):
    def __str__(self):
        return f"{super().__str__()} And I am from coffee sub species."


starbuck = Coffee('Starbuck', 10, Color.BLACK)
print(starbuck)


class Fish(Pet):
    def __str__(self):
        return f"I am a fish named {super().__str__()}"


fish = Fish("Bubbles", 10)
fish.name = 'abc'

# del fish.name

print(f"{fish} {fish.speak()}")

print(f'There are {Pet.get_number_of_pets()} pets.')

for p in [missy, lucky, starbuck, fish]:
    print(repr(p), issubclass(p.__class__, Pet), hash(p))
