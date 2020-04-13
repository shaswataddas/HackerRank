import math
import os
import random
import re
import sys

def countingValleys(n, s):
    level=0
    val_no=0
    for i in range(n):
        if s[i]=="U":
            level+=1
        else:
            level-=1
        if level==0 and s[i]=="U":
            val_no+=1
    return val_no

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
