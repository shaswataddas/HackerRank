import math
import os
import random
import re
import sys

def utopianTree(n):
    n=n+1
    initial_hight=0
    i=0
    for i in range(n):
        if i%2==0:
            initial_hight+=1
        else:
            initial_hight=initial_hight*2
    return initial_hight
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
