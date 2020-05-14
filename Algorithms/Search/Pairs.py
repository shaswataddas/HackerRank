import math
import os
import random
import re
import sys

def pairs(k, arr):
    count=0
    arr.sort()
    for i in arr:
        count=binarySearchAppr(arr,0,len(arr)-1,i+k,count)
    return count

def binarySearchAppr (arr, start, end, x,count):
    if end >= start:
        mid = start + (end- start)//2

        if arr[mid] == x:
            count +=1

        elif arr[mid] > x:
            return binarySearchAppr(arr, start, mid-1, x, count)

        else:
            return binarySearchAppr(arr, mid+1, end, x,count)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
