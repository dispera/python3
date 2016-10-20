#!/usr/bin/env python3

number = str(input("Insert a number: ").strip())
sum = 0

for c in number: sum += int(c)

print("Sum: %i" % sum)