
import math
import os
import random
import re
import sys

def marcsCakewalk(calorie):
    miles=0
    calorie.sort(reverse = True)
    p=0
    for i in calorie:
        miles=miles+((2**p)*i)
        p+=1
    return miles

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
