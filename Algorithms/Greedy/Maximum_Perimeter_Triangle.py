
import math
import os
import random
import re
import sys

def maximumPerimeterTriangle(sticks):
    sticks.sort()
    my_sum = []
    for i in range(len(sticks)-1,1,-1):
        if sticks[i]<sticks[i-1]+sticks[i-2]:
            my_sum.append(sticks[i]+sticks[i-1]+sticks[i-2])
            return   sticks[i-2], sticks[i-1] ,sticks[i]
    return -1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)
    if result!= -1:
        fptr.write(' '.join(map(str, result)))
    else:
        fptr.write(str(result))
    fptr.write('\n')

    fptr.close()
