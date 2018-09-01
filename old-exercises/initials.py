#!/usr/bin/env python3

name = input("Enter your name: ").strip().split()

for i in name:
	print(i[0].upper(),end=' ')