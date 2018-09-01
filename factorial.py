# https://www.hackerrank.com/challenges/30-recursion/problem

def factorial(n):
    if n > 1:
        return n * factorial(n-1) 
    else: 
        return n

print("Enter a positive integer to calculate it's factorial: ",end='')
number = int(input())

print("Factorial of %i: %i" % (number,factorial(number)))
