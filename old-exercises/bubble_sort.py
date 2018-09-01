#!/usr/bin/env python3
#https://www.hackerrank.com/challenges/30-sorting

import sys

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

swaps = 0
for i in range(n):
    for j in range(n-1):
        if a[j] > a[j+1]: 
            a[j],a[j+1] = a[j+1],a[j]
            swaps += 1

print('Array is sorted in %i swaps.\nFirst Element: %i\nLast Element: %i' % (swaps,a[0],a[-1]))
