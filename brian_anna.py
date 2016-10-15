#!/usr/bin/env python3

n,k = map(int,input().strip().split(' '))
lst = list(map(int,input().strip().split()))
b = int(input().strip())

#n,k = 4,1
#lst = [3,10,2,9]
#b = 12

total = 0
for idx in range(len(lst)):
    if idx != k:
        total += lst[idx]

#if sum(lst)/2 > total/2:
if b > total/2:
    print(int(sum(lst)/2 - total/2))
else: print('Bon Appetit')
