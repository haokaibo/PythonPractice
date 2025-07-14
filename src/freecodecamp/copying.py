"""
- shallow copy: one level deep, only references of nested child objects
- deep copy: full independent copy
"""
# copy immutable instance
org = 5
cpy = org
cpy = 6
print(f'org={org}, cpy={cpy}')

# shallow copy mutable instance
org = [0, 1, 2, 3, 4]
cpy = org
cpy[0] = -10
print(f'org={org}, cpy={cpy}')

# one level deep copy mutable instance
import copy

org = [0, 1, 2, 3, 4]
print(f'org={org}, copy.copy(org)={copy.copy(org)}')
# cpy = org.copy()
# print(f'org={org}, org.copy()={cpy}')
# cpy = org[:]
# print(f'org={org}, org[:]={cpy}')
# cpy = list(org)
# print(f'org={org}, list(org)={cpy}')
cpy[0] = -10
print(f'org={org}, cpy={cpy}')

# multilevel deep copy
org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.deepcopy(org)
cpy[0][1] = -10
print(f'org={org}, cpy={cpy}')


# copy on classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Kaibo', 36)
p2 = copy.copy(p1)
p2.age = 28

print(f'p1.age={p1.age}\np2.age={p2.age}')


class Company:
    def __init__(self, boss: Person, employee: Person):
        self.boss = boss
        self.employee = employee

company = Company(p1, p2)
company_clone = copy.deepcopy(company) # copy.copy(company) will maintain the link between the copy to the original object.
company_clone.boss.age = 56
print(f'company_clone.boss.age={company_clone.boss.age}\n'
      f'company.boss.age={company.boss.age}')
