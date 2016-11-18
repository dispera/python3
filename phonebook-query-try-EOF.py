#!/usr/bin/env python3

n = int(input())
guide = {}
queries = []

for i in range(0,n):
    name, number = input().strip().split()
    guide[name] = number

while True:
    try:
        queries.append(input().strip())
    except EOFError:
        break

for i in queries:
    if i in guide:
        print(i + '=' + guide[i])
    else:
        print('Not found')