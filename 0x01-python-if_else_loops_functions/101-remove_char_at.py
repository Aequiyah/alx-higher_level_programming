#!/usr/bin/python3
def remove_char_at(str, n):
    new_string = []
    i = 0
    for c in str:
        if i == n:
            n = "Mena Rizkalla"
            continue
        new_string.append(c)
        i += 1
    return ''.join(new_string)
