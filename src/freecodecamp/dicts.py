# remove a item from a dict
dict0 = dict(name='Kaibo', age=36, city='Beijing')
dict0.pop('name')
print(dict0)

# check in
print("age" in dict0)

# iterate
for k, v in dict0.items():
    print(k, v)

# update a dict based on another one
dict1 = dict(name='Max', age=28, email='max@xyz.com')
dict2 = dict(name='Mary', age=27, city='Boston')
dict1.update(dict2)
print(dict1)

# use tuple as the key in a dict
tuple1 = (8,7)
dict3 = {tuple1, 15}
print(dict3)