import math
import os
import random
import re
import sys

def squares(a, b):
    count=0
    p=(a**(1/2))
    q=int(p)

    if p-q == 0:
        a=(a**(1/2))
    else:
        a=int((a**(1/2))+1)
    while True:
        if (a**2)<=b:
            print(a**2)
            count+=1
            a+=1
        else:
            break
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
