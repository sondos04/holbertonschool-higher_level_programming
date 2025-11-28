#!/usr/bin/python3
from calculator_1 import calculation


if __name__ == "__main__":
    a = 10
    b = 5
    if calculation == 'add':
        calculation = calculation.add
        print("{} + {} = {}".format(a, b, calculation(a, b)))
    elif calculation == 'sub':
        calculation = calculation.sub
        print("{} - {} = {}".format(a, b, calculation(a, b)))
    elif calculation == 'mul':
        calculation = calculation.mul
        print("{} * {} = {}".format(a, b, calculation(a, b)))
    elif calculation == 'div':
        calculation = calculation.div
        print("{} / {} = {}".format(a, b, calculation(a, b))) 
    