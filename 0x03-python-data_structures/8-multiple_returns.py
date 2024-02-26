#!/usr/bin/python3
def multiple_returns(sentence):
    myList = []
    length = len(sentence)
    if (length == 0):
        char = None
    else:
        char = sentence[0]
    myList.append(length)
    myList.append(char)
    return (tuple(myList))
