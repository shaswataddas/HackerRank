import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    aplist=[]
    orlist=[]
    resultapp=0
    resultor=0

    for i in apples:
        aplist.append(a+i)
    for j in oranges:
        orlist.append(b+j)

    for i in aplist:
        if i>=s and i<=t:
            resultapp+=1
    for j in orlist:
        if j>=s and j<=t:
            resultor+=1
    print(resultapp)
    print(resultor)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
