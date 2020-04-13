import math
import os
import random
import re
import sys


def breakingRecords(scores):
    mini=scores[0]
    maxi=scores[0]
    p=0
    q=0
    for i in scores:
        if i<mini:
            mini=i
            p+=1   
        if i>maxi:
            maxi=i
            q+=1
    return(q,p)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
