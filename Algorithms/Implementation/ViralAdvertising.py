import math
import os
import random
import re
import sys

def viralAdvertising(n):
    shared=5
    mysum=0
    while n>0:
        like_no=math.floor(shared/2)
        mysum+=like_no
        shared=like_no*3
        n-=1
    return mysum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
