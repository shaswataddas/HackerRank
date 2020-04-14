import math
import os
import random
import re
import sys

def pangrams(s):
    x="qwertyuiopasdfghjklzxcvbnm"
    x=set(x)
    if(set(s.lower()).intersection(x)==x):
        return("pangram")
    else:
        return("not pangram")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
