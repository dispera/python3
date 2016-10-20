#!/usr/bin/env python3

a, b = [int(n) for n in input("Insert 2 numbers: ").strip().split()]

print("Greatest common divisor for {} and {} is: ".format(a, b),end='')

while b != 0: a, b = b, a % b

print(a)




'''
maxi = 0

if a > b: greater = a
else: greater = b


for i in range(1,greater):
	if a % i == 0 and b % i == 0:
		if i > maxi: maxi = i

print("Greatest common divisor for {} and {} is: {}".format(a, b, maxi))
'''
