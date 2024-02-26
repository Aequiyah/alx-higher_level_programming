#!/usr/bin/python3
from functools import reduce
print(reduce(lambda x, y: x + y, list(map(lamba x: chr(x), range(65, 91)))))
