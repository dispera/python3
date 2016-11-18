#!/usr/bin/env python3
from sys import argv

print('REMAINING DOWNLOAD TIME CALCULATOR\n')
print('Enter download size in GB: ',end='')
size = float(input())
print('Enter download speed in KB/s: ',end='')
speed = int(input())

hrs_remaining = ( (size * 1024 * 1024) / speed ) / 60 / 60
mts_remaining = hrs_remaining * 60
if mts_remaining > 60:
    print('Remaining time: %d hours and %2d minutes (or a total of %d minutes)' % (hrs_remaining, mts_remaining % 60, mts_remaining))
else:
    print('\nRemaining time: %2d minutes' % (mts_remaining))
