#!/usr/bin/python3
def replace_in_list(my_list, index, element):
    if (0 <= index < len(my_list)):
        my_list[index] = element
    return my_list
