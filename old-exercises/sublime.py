#!/usr/bin/env python3
# This is for quora upvotes coding challenge: https://www.quora.com/about/challenges

for y in range(2016,2090):
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        print("The year %i is a Leap Year" % y)



