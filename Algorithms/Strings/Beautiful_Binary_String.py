
import math
import os
import random
import re
import sys

def beautifulBinaryString(b,count):
    
    if "010" in b:
        copy= b
        b=b.replace("010","")
        count = (len(copy)-len(b))/3
    return int(count)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    count=0
    n = int(input())

    b = input()

    result = beautifulBinaryString(b,0)

    fptr.write(str(result) + '\n')

    fptr.close()
