#!/usr/bin/env python3
import sys

class Difference:
    def __init__(self, a):
        self.elements = a

        # Add your code here
    def computeDifference(self):
    	self.maximumDifference = 0
    	iteration = 0
    	for i in range(iteration,len(self.elements)):
    		for j in range(iteration,len(self.elements)):
    			diff = self.elements[i] - self.elements[j] 
    			if diff < 0: diff = diff * -1
    			if diff > self.maximumDifference: 
    				self.maximumDifference = diff
    		iteration += 1


        

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)