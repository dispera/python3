#!/usr/bin/env python3

# implemented while instead of 2 for loops, each pass it gets the biggest number to the end
# and when it reaches the end, next pass goes to one index less than that last end.

import sys
import random
import time
start_time = time.time()

a = []
for i in range(1,22000):
    a.append(i)

random.shuffle(a)

print(a)

last_biggest = len(a)-1

while last_biggest > 0:
    for i in range(0,last_biggest):
        if a[i] > a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
    last_biggest -= 1

print(a)
print("Time elapsed: {:.2f}s".format(time.time() - start_time))

