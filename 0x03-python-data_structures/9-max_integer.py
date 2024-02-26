#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    maximum = my_list[0]
    for item in my_list:
        if item > maximum:
            maximum = item
    return maximum
