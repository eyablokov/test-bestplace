#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Median of numbers.

This script takes three numbers as arguments and returns middle number.

Example:
    ./median.py 334 9 1122
"""

import sys
from numpy import array, median

if len(sys.argv) != 4:
    print("Enter 3 numbers as arguments")
    exit()

items = []

for i in range(1, 4):
    items.append(sys.argv[i])

items = sorted(items, key=int)

nums = [int(x) for x in items]

def mediana(nums):
    """ Using numpy module to get a median. """
    return print(int(median(array(nums))))

mediana(nums)
