
import math
import os
import random
import re
import sys


def permutationEquation(p):
    test_p=list(set(p))
    count=0
    while(count<2):
        for i in range(len(test_p)):
            for j in range(len(p)):
                if test_p[i]==p[j]:
                    test_p[i]=j+1
                    break
        count+=1
    return test_p

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))

    fptr.write('\n')

    fptr.close()
