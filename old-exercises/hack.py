#!/usr/bin/env python3
'''
import sys


a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

a_score = 0
b_score = 0

a_list = [a0,a1,a2]
b_list = [b0,b1,b2]

for i in range (0,3):
    if a_list[i] > b_list[i]:
        a_score += 1
    elif a_list[i] < b_list[i]:
        b_score += 1

print(a_score, b_score)
'''
####
'''
import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

def calc_total(array):
    total = 0
    for i in array:
        total += i
    return total

print (calc_total(arr))
'''
###
'''
Given a square matrix of size , calculate the absolute difference between the sums of its diagonals.

Input Format

The first line contains a single integer, . The next  lines denote the matrix's rows, with each line containing  space-separated integers describing the columns.
'''
'''
import sys
from math import sqrt

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

sum_a = 0
sum_b = 0
cols = n

#Go through first diagonal
for i in range(n):
    for j in range(cols):
        if i == j: sum_a += a[i][j]

index_i = n-1
index_j = 0

for i in range(n):
    sum_b += a[index_i][index_j]
    index_i -= 1
    index_j += 1

result = int(sqrt((sum_a - sum_b) * (sum_a - sum_b)))
print(result)
'''
###
'''
lst = [int(input()), int(input())]
print (lst[0] + lst[1])
print (lst[0] - lst[1])
print (lst[0] * lst[1])
'''
###
'''
N = int(input())
map(lambda x: print(x,),N)
'''

#N = int(input())
'''
print(123),
for i in range(4,N+1):
    print(i,)
    '''
#for i in range(1,N+1):
#    print(i, end="")

############ RESOLVE LATER!! ############
#map(lambda i: print(i, end=""),range(10))
###

## LISTS!!!!####
'''
lst = []
times = int(input())

def insert(i, e):
    lst.insert(i, e)


for i in range(0,times):
    cmd = input().split()
    c0 = cmd[0]
    if len(cmd) > 1: c1 = int(cmd[1])
    if len(cmd) > 2: c2 = int(cmd[2])

    if c0 == 'insert':
        lst.insert(c1,c2)
    if c0 == 'print':
        print(lst)
    if c0 == 'remove':
        lst.remove(c1)
    if c0 == 'append':
        lst.append(c1)
    if c0 == 'sort':
        lst.sort()
    if c0 == 'pop':
        lst.pop()
    if c0 == 'reverse':
        lst.reverse()
'''
###
'''
times = int(input())
lst = input().split()
for i in lst:
    lst[i] = int(i)
t = tuple(lst)
print(hash(t))
'''
#GOOD ONE< HARD#
'''Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid. You have to print a list of all possible coordinates on a 3D grid where the sum of      is not equal to . If , the possible values of  can be ,  and . The same applies to  and .

Input Format

Four integers  and  each on four separate lines, respectively.

Output Format

Print the list in lexicographic increasing order.

Sample Input

1
1
1
2
Sample Output

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
'''
# didnt use this: from itertools import permutations
'''
X, Y, Z, N = [int(input()),int(input()),int(input()),int(input())]
# For Testing:
#X, Y, Z, N = [1,1,1,2]

lst = []
for x in range(0,X+1):
    for y in range(0,Y+1):
        for z in range(0,Z+1):
            lst.append([x,y,z])

lexi_list = [x for x in lst if sum(x) != N]
print(lexi_list)
'''
#Find the Second Largest Number
'''
N = int(input())
array = list(map(int,input().split()))

array.sort()
array.reverse()

uniqs = []
for i in array:
    if i not in uniqs:
        uniqs.append(i)

print(uniqs[1])
'''
'''Alex has a habit of falling asleep during lectures! In order to complete the day's homework, he must determine if he has any friends that stayed awake so he can borrow their notes.

There are  other students in Alex's class, and each student has a distinct ID number from  to . You are given a string, , of  binary characters where the  character denotes whether the student slept during the lecture or not. If the  character is a , then the  student stayed awake and took notes; otherwise, the  character is a  which indicates the student fell asleep and did not take notes.

Alex has  friends in his class and you are given a list of integers corresponding to their respective ID numbers. If Alex can borrow the lecture notes from one of his friends, print YES; otherwise, print NO.

Input Format

The first line contains two space-separated integers denoting the respective values of  (the number of students in Alex's class) and  (Alex's number of friends in the class).
The second line contains a single binary string (i.e., 's and 's) of length . If the  character is a , then Alex can't get notes from them; otherwise, it's a , indicating the  student took lecture notes.
The next line contains  distinct space-separated integers where each integer denotes the ID number of one of Alex's friends.

Constraints


Output Format

Print YES on a new line if Alex can get the lecture notes from one of his friends; otherwise, print NO.

Sample Input

3 2
101
1 3
Sample Output

NO
Explanation

There are  other students in the class, and  of them are Alex's friends. Students  and fell asleep, but student  stayed awake. Alex is only friends with students  and  and, as they both fell asleep during the lecture, Alex cannot get notes from them. Thus, we print NO as our answer.
'''
'''
#!/bin/python3
import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
s = input().strip()
friends = [int(friends_temp) for friends_temp in input().strip().split(' ')]

have_notes = 'NO'
for i in range(n):
    if s[i] == '0' and ((i+1) in (friends)):
        have_notes = 'YES'

print (have_notes)
'''

#!/bin/python3
import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]

P = []
D = []

for x in range(n):
    pn,dn = input().strip().split(' ')
    P.append(pn)
    D.append(dn)

score = []

for i in range(n):
    current_score = int(P[i]) - int(D[i])
    score.append([current_score,i])

score.sort()
score_increasing = score[:]
score.reverse()
zigzag = []
for i in range(len(score)):
    zigzag.append(score[i])
    zigzag.append(score_increasing[i])

absol_array = []
for i in range(n):
    tmp = score[i]
    x1,x2 = [int(tmp[0]), int(tmp[1])]
    absol_array.append([abs(x1),x2])

absol_array.sort()
absol_array.reverse()

#score_hash = {}
'''
max_gain = 0
for i in range(k):
    #score_hash[i] = score[i[0]]
    t1 = zigzag[i]
    t2 = t1[1]
    t2 = int(t2)
    max_gain += int(P[t2])
'''
max_gain = 0
for i in range(k):
    #score_hash[i] = score[i[0]]
    t1 = absol_array[i]
    t2 = t1[1]
    t2 = int(t2)
    max_gain += int(P[t2])


#print(P, '\n', D)
#print(score)
#print(max_gain)

'''
deductions = 0
for i in zigzag[k:n]:
    t1 = i[:]
    t2 = t1[1]
    t2 = int(t2)
    deductions += int(D[t2])
'''
deductions = 0
for i in absol_array[k:n]:
    t1 = i[:]
    t2 = t1[1]
    t2 = int(t2)
    deductions += int(D[t2])

if n > k:
    max_gain_w_ded = max_gain - deductions
    if max_gain_w_ded > 0:
        print (max_gain_w_ded)
    else: print('0')
else:
    max_gain_w_ded = max_gain
