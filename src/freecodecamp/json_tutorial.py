import json

person = {"name": "John", "age": 30, "city": "New York",
          "hasChildren": False, "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('Kaibo', 36)


def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type user is not JSON serializable.')

userJSON = json.dumps(user, default=encode_user)
print(userJSON)

# JSONEncoder
from json import JSONEncoder


class UserEncoder(JSONEncoder):
    def default(self, o: User) -> dict:
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__:True}
        return JSONEncoder.default(self, o)

userJSON = UserEncoder().encode(user)
print(userJSON)

def decode_user(dic):
    if User.__name__ in dic:
        return User(name=dic['name'], age=dic['age'])
    return dic

user = json.loads(userJSON, object_hook=decode_user)
print(type(user))