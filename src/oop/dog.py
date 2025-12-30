
from typing import ClassVar

class Dog:
    '''
    This class 
    '''
    target: str
    toys: list[str]

    ### Define the class level attribute
    max_life: ClassVar[int] = 20

    def __init__(self, target: str = "socks", toys: list[str] | None = None):
        self.target = target

        ### Init the toys attribute as empty array when the input is None
        if toys is None:
            self.toy = []
        else:
            self.toys = toys
    

Dog.max_life = 100
dog = Dog()


def add(a: int, b: int): 
    return a + b
 
add(3, 4)


if __name__ == '__main__':
    add(1,2)
    add(a, c)


### The class attribute [max_life] cannot be set by instance

# dog.max_life = 2  

#%%

a: int = 1
b: int = 2
# %%
print(b)
#%%