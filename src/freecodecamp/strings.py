# Strings: orderd, immutable, text representation
str1 = "I'm a programmer"
print(str1)
print(str1[0])
print(str1[1:5])
print(str1[::-1])
print("a" + 'b')
for c in str1:
    print(c)
if 'e' in str1:
    print('Yes')
else:
    print('no')

# trim
str2 = '  Hello world. '
str3 = str2.strip()
print(f'str2={str2}\nstr3={str3}')

#  find
print(f"str2.find('o')={str2.find('o')}")

# count
print(f"str2.count('l')={str2.count('l')}")

# concatenate
from timeit import default_timer as timer

my_list = ['a'] * 100000
print(f'my_list={my_list}')

start = timer()
my_string = ''
for i in my_list:
    my_string += i
stop = timer()
print(f'It took {stop - start}s to concatenate the string.')

start = timer()
my_string = ''.join(my_list)
stop = timer()
print(f'It took {stop - start}s to concatenate the string.')

# format
var = "Kaibo"
f = 3.1415926
my_string = "The variable is %s. The f is %.2f" % (var , f)
print(my_string)
my_string = "The variable is {:s}. The f is {:.2f}".format(var, f)
print(my_string)
my_string = f"The variable is {var}. The f is {f:.2f}"
print(my_string)

