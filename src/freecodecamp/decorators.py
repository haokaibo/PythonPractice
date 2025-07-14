import functools


def decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper


@decorator1
def print_name():
    print('Kaibo')


print_name()


@decorator1
def add5(x):
    return x + 5

print(f'add5(10)={add5(10)}')

print(help(add5))
print(add5.__name__)


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}.')

greet('Kaibo')

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
        signature = ','.join(args_repr + kwargs_repr)
        print(f'Calling {func.__name__!r}({signature})')
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

@debug
@decorator1
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

say_hello('Kevin')

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls+=1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)

@CountCalls
def do_something():
    print('Call do something.')

for i in range(2):
    do_something()

@CountCalls
def do_something2():
    print('Call do something 2.')

for i in range(2):
    do_something2()