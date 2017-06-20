#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Punctured array.

This script returns the number removed from the array.

Example:
    ./punctured_array.py 9
"""

import sys
import random

if len(sys.argv) != 2:
    print("Enter one number as an argument")
    exit()

# Initialize the original array
lastElement = int(sys.argv[1])
origin = list(range(1, lastElement + 1))
arr = list(range(1, lastElement + 1))

# Shuffle and pop the forked array
random.shuffle(arr)
arr.pop(random.randrange(len(arr)))

def find_missing(origin, arr):
    """ This function gets two lists - 'origin' and 'arr' as arguments. Then it
    makes a 'copy' list, which is the same to 'arr'. Using 'current' loop
    pointer, it passes through the 'origin' list, and going to compare if each
    cell exists in the 'copy' list. If not - show it. """
    copy = list(arr)
    for current in origin:
        if current not in copy:
            return print('Removed number is:', current, '| the list generated is:', copy)

find_missing(origin, arr)
