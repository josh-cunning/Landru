from __future__ import unicode_literals, absolute_import, print_function, division

import random
import re
import operator
import sopel.module
import operator
import sopel.module


def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return  False

def randprice(max):
    if max < 1:
        max = 5
    price = txt = random.randint(0, max)
    return price
