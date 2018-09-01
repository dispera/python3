#!/usr/bin/env python3
import sys

arr = []

for i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

max = -63

for row in range(0,4):
	for col in range(0,4):
		hourglass = arr[row][col] + arr[row][col+1] + arr[row][col+2] + \
					arr[row+1][col+1] + \
					arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]

		if hourglass > max: max = hourglass

print(max)
