# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter

a = 'aaaaabbbbccc'
counter = Counter(a)
print(counter)
print(f'counter.most_common(1)={counter.most_common(1)}')
print(list(counter.elements()))

from collections import namedtuple

Point = namedtuple('Point', 'x,y,z')
pt = Point(1, -4, 2)
print(f'x={pt.x}, y={pt.y}, z={pt.z}')

from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['a'] = 1
print(ordered_dict.items())

from collections import defaultdict

default_dict = defaultdict(int)
default_dict['a'] = 1
default_dict['b'] = 2
print(f"default_dict['c']={default_dict['c']}")

from collections import deque

d = deque()
d.append(1)
d.append(2)
d.appendleft(0)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.extendleft([4, 5, 6])
print(d)
d.rotate(1)
print(d)
d.rotate(-1)
print(d)
