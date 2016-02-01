# Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
import os
os.chdir('C:\Kaibo\PythonPractice\HeadFirstPython\chapter3')
os.getcwd()
data = open('sketch.txt')
print(data.readline(), end='')
data.seek(0)
for each_line in data:
    try:
        (role, line_spoken) = each_line.split(':', 1)
        print(role, end='')
        print(' said: ', end='')
        print(line_spoken, end='')
    except:
        pass
data.close();
