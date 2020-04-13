import math
import os
import random
import re
import sys

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    p=0
    if n>=6:
        arr=[0,0,0,0]
        for i in password:
            if i in special_characters:
                arr[0]+=1
            elif i in lower_case:
                arr[1]+=1
            elif i in upper_case:
                arr[2]+=1
            else:
                arr[3]+=1
        for i in arr:
            if i==0:
                p+=1
            
    else:
        k=6-n
        arr=[0,0,0,0]
        for i in password:
            if i in special_characters:
                arr[0]+=1
            elif i in lower_case:
                arr[1]+=1
            elif i in upper_case:
                arr[2]+=1
            else:
                arr[3]+=1
        for i in arr:
            if i==0:
                p+=1
        if k>=p:
            return k
    return p



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
