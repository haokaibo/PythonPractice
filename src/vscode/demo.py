class Person:

    def call(self, name):
        print(f'Find a job now! {name}')

class HR(Person):
    def call(self, name):
        print('I am an HR. ')
        super().call(name)


# def __init__(self, r=None):
#         self.root = r
#         self.size = 0

if __name__ == "__main__":
    p = HR()
    p.call('Kaibo')


