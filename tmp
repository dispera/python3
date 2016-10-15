#!/usr/bin/env python3

import sys
from math import ceil

s = input().strip()
n = int(input().strip())

a_in_word = 0
for c in s:
    if c == 'a': a_in_word += 1

words_to_repeat = int( n / len(s) )

a_in_module = 0
letters_left = int(n % len(s))
if letters_left > 0:
    for c in s:
        if c == 'a': a_in_module += 1
        letters_left -= 1
        if letters_left == 0: break

total_a = (a_in_word * words_to_repeat) + a_in_module

print(total_a)
