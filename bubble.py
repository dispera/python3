#!/bin/python3
#https://www.hackerrank.com/challenges/30-sorting/problem

import sys

#n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

totSwaps = 0
for i in range(len(a)):
    numSwaps = 0
    for j in range(len(a) - 1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            numSwaps += 1
            totSwaps += 1
    if numSwaps == 0: break
        
print("Array is sorted in %i swaps." % totSwaps) 

print("First Element: %i" % a[0]) 

print("Last Element: %i" % a[len(a) - 1])