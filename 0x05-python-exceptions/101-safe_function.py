#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as error:
        print(f"Exception: {error}", file=sys.stderr)
        return None
