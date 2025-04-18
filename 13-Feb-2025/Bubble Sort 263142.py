# Problem: Bubble Sort - https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    num_of_swaps = 0
    n = len(a)
    for i in range(n):
        swapped = False
        
        for j in range(n-1):
            if a[j] > a[j+1]:
                num_of_swaps += 1
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
                
        if not swapped:
            break
                
    print(f"Array is sorted in {num_of_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
