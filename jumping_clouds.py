#!/usr/bin/env python3
#https://www.hackerrank.com/challenges/jumping-on-the-clouds
import sys

#n = int(input().strip())
#c = [int(c_temp) for c_temp in input().strip().split(' ')]
n = 85
c = [int(c) for c in ('0 1 0 1 0 1 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 1 0 1 0 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 1 0 1 0 0 0 1 0 0 0 0 0 1 0 1 0 1 0 0 1 0 1 0 1 0 0 1 0 0 0 0 1 0 0 1 0 0 0 1 0 0 1 0 1 0').split()]

total_jumps = 0
bonus_count = 0

for i in range(0,len(c)):
    if c[i] == 0:
        total_jumps += 1
        bonus_count += 1
        if bonus_count == 3:
            bonus_count = 1
            total_jumps -= 1
    elif c[i] == 1:
        bonus_count = 0

print(total_jumps-1)
