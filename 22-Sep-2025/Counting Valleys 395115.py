# Problem: Counting Valleys - https://www.hackerrank.com/challenges/counting-valleys/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    sealevel = 0
    valley = False
    ans = 0
    
    for x in path:
        if x == "U":
            sealevel += 1
        else:
            sealevel -= 1
            
        if sealevel < 0 and not valley:
            valley = True
        elif sealevel >= 0 and valley:
            valley = False
            ans += 1
            
    return ans
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
