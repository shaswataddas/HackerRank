import math
import os
import random
import re
import sys

def gradingStudents(grades):
    result=[]
    for i in grades:
        if i <38:
            result.append(i)
        elif i%5 < 3:
            result.append(i)
        else:
            result.append(i+(5-(i%5)))
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
