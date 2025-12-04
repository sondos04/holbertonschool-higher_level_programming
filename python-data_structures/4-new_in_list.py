#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(len(my_list)):
        if i < 0 or i >= len(my_list):
            return None
        if i == idx:
            new_list = my_list.copy()
            return new_list[i]