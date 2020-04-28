
import math
import os
import random
import re
import sys

def designerPdfViewer(h, word):
    maxi=1
    for i in word:
        index = ord(i)-96
        if h[index-1]>maxi:
            maxi=h[index-1]
    return(len(word)*maxi)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
