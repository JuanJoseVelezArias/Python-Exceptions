#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    
    try:
        aux = value / 1
        print(aux)
        return True
    except TypeError as e:
        print(f"Exception: {e}",  file=sys.stderr)
        return False
