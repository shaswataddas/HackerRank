
import math
import os
import random
import re
import sys

def superDigit(n, k):
    sd = sum(int(s) for s in n)
    if sd*k < 10:
        return sd*k
    else:
        return superDigit(str(sd*k), 1)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
