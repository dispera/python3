#!/usr/bin/env python3

N = int(input().strip())
S = [input().strip() for x in range(N)]
#S = ['acxz', 'bcxz']
R = [r[::-1] for r in S]

for i in range(N):
    funny = 1
    for c in range(len(S[i])):
        if c> 0 and (abs(ord(S[i][c]) - ord(S[i][c-1]))) != abs((ord(R[i][c]) - ord(R[i][c-1]))) :
            print('Not Funny')
            funny = 0
            break
    if funny == 1: print('Funny')

