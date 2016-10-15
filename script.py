#!/usr/bin/env python3
'''
V = int(input().strip())
n = int(input().strip())
ar = input().strip().split()
'''
V = 4
n = 6
ar = '1 4 5 7 9 12'.split()

for idx in range(0,n):
    if int(ar[idx]) == V: print(idx)
