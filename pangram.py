#!/usr/bin/env python3

import string
alphabet = list(string.ascii_lowercase)

lst = input().strip()

for c in lst:
    char = c.lower()
    if char in alphabet:
        alphabet.remove(char)
        
if len(alphabet) == 0:
    print('pangram')
else:
    print('not pangram')
