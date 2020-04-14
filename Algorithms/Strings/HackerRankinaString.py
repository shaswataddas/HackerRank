import math
import os
import random
import re
import sys

def hackerrankInString(s):
    count=0
    word=['h','a','c','k','e','r','r','a','n','k']
    for i in s:
        if i==word[0]:
            count+=1
            print(word[0])
            word.remove(word[0])
            if count==10:
                return("YES")
    if len(word)==0:
        return("YES")
    else:
        return("NO")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
