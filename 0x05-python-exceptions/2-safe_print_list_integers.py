#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for i in range(x):
        if not isinstance(my_list[i], int):
            continue
        try:
            print("{:d}".format(my_list[i]), end="")
            counter += 1
        except Exception:
            continue
    print()
    return counter
