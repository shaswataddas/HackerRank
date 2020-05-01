
import math
import os
import random
import re
import sys


def funnyString(s):
    mylist=[]
    revlist=[]
    rev_s=s[::-1]                                     # Reverse the string
    for i in range(len(s)-1):
        j=i+1
        mylist.append(abs((ord(s[j])-ord(s[i]))))
        revlist.append(abs((ord(rev_s[j])-ord(rev_s[i]))))

    for i in range(len(mylist)):
        if (mylist[i]-revlist[i])!=0:
            return("Not Funny")
        if i==len(mylist)-1:                           # When the Every elements of the list is checked
            return("Funny")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result+ '\n')


    fptr.close()
