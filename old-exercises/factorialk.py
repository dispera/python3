#!/usr/bin/env python3

N = int(input())
'''
def factorial(number,total):
    if number <= 1:
        print(total)
        #return total
    else:
        total = total * (number - 1)
        factorial(number - 1, total)

#result = factorial(N, N)

#print(result)
'''
def factorial(n):
    if n == 1: #checked online example and it was n==0 but I believe stopping at 1 works as this mult is useless
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(N))
