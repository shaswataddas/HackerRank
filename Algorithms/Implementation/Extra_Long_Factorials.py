
import math
import os
import random
import re
import sys

def extraLongFactorials(n):
    if n==0:
        return 1
    else:
        return n*extraLongFactorials(n-1)
if __name__ == '__main__':
    n = int(input())

    result=extraLongFactorials(n)
    print(result)
