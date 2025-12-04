#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    for i in range(len(my_list)):
        if i < 0 or i >= len(my_list):
            return my_list
        if i == idx:
            new_list = my_list.copy()
            new_list[i] = element
            return new_list