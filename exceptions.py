#!/bin/python3

import sys

print("Enter a string and we will try to convert it into an integer")
S = input().strip()

try:
    print(int(S))
except ValueError:
    print("Bad String")
