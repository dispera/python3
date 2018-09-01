#!/usr/bin/env python3
'''
T = int(input().strip())
S = [input().strip() for x in range(0,T)]

for i in S:
    evens, odds = ['','']
    for idx in range(0,len(i)):
        if idx % 2 == 0 or idx == 0: evens += i[idx]
        else: odds += i[idx]
    print(evens,odds)
    '''
'''
S = input().strip()
unique = ''

for idx in range(0, len(S) - 1):
    if S[idx] == S[idx + 1]:
        pass
    else:
        unique += S[idx]
if S[len(S) - 1] == S[len(S) - 2]: unique += S[len(S) - 1]

if unique == '':
    print('Empty String')
else:
    print(unique)

'''

S = input().strip()
nu = []
for i in S:
    nu.append(i)

try:
    for idx in range(0,len(uniques)):
        try:
            if uniques[idx] == uniques[idx+1]:
                uniques.pop(idx)
                uniques.pop(idx+1)

if uniques == '':
    print('Empty String')
else:
    print(uniques)
