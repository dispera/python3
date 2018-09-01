#!/usr/bin/env python3

bits = int(input("Bit Counter - Enter number of bits: ").strip())
total = 0

for i in range(0,bits):
    curr_bits = 2**i
    print("BIT %2i: %20i" % (i+1,curr_bits))
    
    total += curr_bits

print("Total number you can store in %i bits: %i" % (bits, total))
    
