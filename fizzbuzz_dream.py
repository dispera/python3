#!/usr/bin/env python3
#implementation I dreamed

def fizzBuzz(n):
	for i in range(1,n+1):
		output = ''
		fizzFlag = False

		if i % 3 == 0: 
			output += 'Fizz'
			fizzFlag = True

		if i % 5 == 0: output += 'Buzz'
		
		elif fizzFlag == False: output = i

		print(output, end=' ')

#limit = int(input("Please enter a limit for FizzBuzz: "))
limit = 10000000

fizzBuzz(limit)

