import random

a = random.random()
print(f'random.random()={a}')

a = random.randint(1, 10)
print(f'random.randint(1, 10)={a}')

a = random.randrange(1, 10)
print(f'random.randrange(1, 10)={a}')

a = random.normalvariate(0, 1)
print(f'random.normalvariate(0, 1)={a}')

list1 = list('ABCDEFGH')
a = random.choices(list1, k=3)
print(a)

random.shuffle(list1)
print(list1)

# fake random
random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(2)
print(random.random())
print(random.randint(1,10))
random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(2)
print(random.random())
print(random.randint(1,10))
# genuine random
import secrets

a = secrets.randbelow(10)
print(a)

a =secrets.randbits(4)
print(a)

list2 = list('ABCDEFGH')
a = secrets.choice(list2)
print(a)

import numpy as np
a = np.random.rand(3)
print(a)

a = np.random.randint(0, 10, (3,4))
print(a)

np.random.shuffle(a)
print(a)

np.random.seed(1)
print(np.random.rand(3,3))

np.random.seed(1)
print(np.random.rand(3,3))