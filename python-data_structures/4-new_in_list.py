#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element in a list at a specific index without modifying the original list.

    Args:
        my_list (list): The original list.
        idx (int): The index of the element to replace.
        element: The new element to insert at the specified index.

    Returns:
        list: A new list with the specified element replaced, or the original list if the index is out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list[:] # : = copy all elements
    
    new_list = my_list[:]
    new_list[idx] = element
    return new_list