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
