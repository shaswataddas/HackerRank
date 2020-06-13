import math
import os
import random
import re
import sys

def theLoveLetterMystery(s):
    count=0
    for i in range(int((len(s)/2))):
        if s[i]!=s[len(s)-i-1]:
            print(s[i],s[len(s)-i-1])
            count += abs(ord(s[i])-ord(s[len(s)-i-1]))
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
