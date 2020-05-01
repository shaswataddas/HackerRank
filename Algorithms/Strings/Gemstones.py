
import math
import os
import random
import re
import sys

def gemstones(arr):
    count=0
    mylist=set(list(arr[0]))                            # save the letters for compare with other arr elements
    for i in mylist:                                    # pick each element from mylist & compare
        for j in range(1,len(arr)):
            if i not in arr[j]:
                break                                   # If any letter not match then come out from that element
            if j == len(arr)-1:                         # when all the elemenrs are checherd
                count+=1
    return count                                        # Return the value
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
