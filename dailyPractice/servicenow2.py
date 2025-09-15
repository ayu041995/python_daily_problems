#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'groupDivision' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY levels
#  2. INTEGER maxSpread
#

def groupDivision(levels, maxSpread):
    # Write your code here
    # print('me')
    levels.sort()
    groups = 0
    i = 0
    n = len(levels)
    
    while i < n:
        # print(i)
        groups += 1
        
        start = levels[i]
        while i < n and   levels[i] - start <= maxSpread:
            i += 1
    return groups     
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    levels_count = int(input().strip())

    levels = []

    for _ in range(levels_count):
        levels_item = int(input().strip())
        levels.append(levels_item)

    maxSpread = int(input().strip())

    result = groupDivision(levels, maxSpread)

    fptr.write(str(result) + '\n')

    fptr.close()