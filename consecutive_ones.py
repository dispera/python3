# based on https://www.hackerrank.com/challenges/30-binary-numbers/problem

print("Enter a number and I will tell you,")
print("the maximum consecutive 1's on it's binary representation: ", end='')
n = int(input())

consecutive_ones = 0
max_consecutive_ones = 0
is_consecutive = 1
bin_string = str(bin(n))

for d in range(2,len(bin_string)):
    if bin_string[d] == '1':
        if is_consecutive == 1: 
            consecutive_ones += 1
        else: consecutive_ones = 1
        is_consecutive = 1
        if consecutive_ones > max_consecutive_ones:
            max_consecutive_ones = consecutive_ones
    else:
        is_consecutive = 0
        consecutive_ones = 0

print("Binary representation: %s" % bin_string[2::])
print("Maximum consecutive 1s: %i" % max_consecutive_ones)
