#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    remainder = [0] * k
    for i in s:
        remainder [i% k] += 1
        
    maxnum = 0
    maxnum += min(remainder [0], 1)
    if k%2 == 0:
        maxnum += min(remainder [k//2], 1)
        
    for i in range(1, k//2 + 1):
        if i != k-i:
            maxnum += max(remainder [i], remainder [k-i])
    return maxnum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
