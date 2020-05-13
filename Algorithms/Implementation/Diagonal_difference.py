
import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    sum1=0
    sum2=0
    for i in range(len(arr)):
        sum1=sum1+arr[i][i]
        sum2=sum2+arr[i][abs(i-len(arr)+1)]   
    return abs(sum1-sum2)  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
