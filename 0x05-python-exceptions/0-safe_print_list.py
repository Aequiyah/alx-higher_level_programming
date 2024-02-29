#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for item in my_list:
            if counter == x:
                break
            counter += 1
            print(item, end="")
        print()
        return counter
    except Exception:
        return 0
