
import math
import os
import random
import re
import sys

def balancedSums(arr):
    
    if len(arr)==1:
        return("YES")
    
    else:
        for i in range(len(arr)):
            suml=0
            sumr=0
            for j in range(0,i):
                suml=suml+arr[j]
            for k in range(i+1,len(arr)):
                sumr=sumr+arr[k]
            if suml == sumr:
                return("YES")
    return("NO")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
