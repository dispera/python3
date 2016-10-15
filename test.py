#!/usr/bin/env python3

import sys
'''
s = 'saveChangesInTheEditor' #input().strip()

lst = [i for i in s if i == i.upper()]

print(len(lst)+1)
'''
import string
alphabet = list(string.ascii_lowercase)

#lst = 'The quick brown fox jumps over the lazy dog'
lst = 'BATMAN'
total = len(alphabet)
for c in lst:
    char = c.lower()
    if char in alphabet:
        alphabet.remove(char)

print ('Letters of the alphabet used: ', total - len(alphabet))
