
import math
import os
import random
import re
import sys


def missingNumbers(arr, brr):
    for i in arr:
        brr.remove(i)
    brr=set(brr)
    brr= list(brr)
    brr.sort()
    return brr
     
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
