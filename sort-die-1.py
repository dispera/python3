#!/usr/bin/env python3

import sys
import random
import time
start_time = time.time()

a = []
for i in range(1,22000):
    a.append(i)

random.shuffle(a)

print(a)


for i in range(0,len(a)-1):
    for i in range(0,len(a)-1):
        if a[i] > a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]

print(a)
print("Time elapsed: {:.2f}s".format(time.time() - start_time))
