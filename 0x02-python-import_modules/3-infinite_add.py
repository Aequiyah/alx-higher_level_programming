#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv) - 1
    summation = 0
    for i in range(length + 1):
        if i == 0:
            continue
        summation += int(sys.argv[i])
    print(summation)
