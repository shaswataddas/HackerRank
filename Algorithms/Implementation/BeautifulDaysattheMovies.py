import math
import os
import random
import re
import sys

def beautifulDays(i, j, k):
    temp=0
    while i<=j:
        rev=str(i)[::-1]
        diff=i-int(rev)
        if diff%k==0:
            temp+=1
        i+=1
    return temp

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
