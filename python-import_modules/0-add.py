#!/usr/bin/python3
def add(a, b):
    return a + b


#!/usr/bin/env python3
add = __import__('0-add').add
a = 1
b = 2
print( a, " + ",b," = ",add(a, b))