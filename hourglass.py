#!/bin/python3
# https://www.hackerrank.com/challenges/30-2d-arrays/problem

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

max_hourglass = -63 # Minimum possible hourglass of all -9
for x in range(4):
    for y in range(4):
        current_hourglass = arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+1] + arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]
        if current_hourglass > max_hourglass:
            max_hourglass = current_hourglass

print(max_hourglass)