#!/usr/bin/env python3

import sys

for n in range(1,10100000):
    if n % 3 == 0: print('Fizz',end='')
    if n % 5 == 0: print('Buzz',end='')        
    elif n % 3 != 0: print(n,end='')

    print(' ',end='')

'''
for n in range(1,101):
    output = ''
    if n % 3 == 0: output += 'Fizz'
    if n % 5 == 0: output += 'Buzz'
    elif n % 3 != 0: output = n
    print(output)
'''