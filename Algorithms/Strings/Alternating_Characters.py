
import math
import os
import random
import re
import sys

def alternatingCharacters(s):
    count=0
    i=0
    s=list(s)
    while i < (len(s)-1):
        j=i+1
        if s[i]==s[j]:                                         # If the Adjacent two elements are same
            s.remove(s[j])                                              # Remove the same element
            count+=1                                                    # Incremnt Result by 1
        else:
            i+=1                                               # Else increment the index value by 1
    return count                                            # RETURN result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
