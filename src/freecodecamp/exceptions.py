# Errors and Excpetions
# x = - 5
# if x< 0:
#     raise Exception('x should be greater than or equals to 0.')

# x = -5
# assert (x>=0), 'x should be greater than or equals to 0.'

try:
    a = 5/ 0
except ZeroDivisionError as e:
    print(f'an error({e}) happened.')

try:
    a = 'a'+'10'
except ZeroDivisionError as e:
    print(f'an error({e}) happened.')
except TypeError as e:
    print(f'{e}')
else:
    print('everything is fine')
finally:
    print('cleaning up...')


class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high.')
    if x< 5:
        raise ValueTooSmallError('value is too small.', x)

try:
    test_value(200)
except ValueTooHighError as e:
    print(e)

try:
    test_value(1)
except ValueTooSmallError as e:
    print(e.message, e.value)