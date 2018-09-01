#!/usr/bin/env python3
# A pangram is a string that contains all the letters
# of the alphabet at least once.
# Known pangram in english:
# The quick brown fox jumps over the lazy dog

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
