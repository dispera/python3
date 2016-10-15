#!/usr/bin/env python3
# This is for quora upvotes coding challenge: https://www.quora.com/about/challenges

# I read the input below to store N, K, and an array with integers for the upvote counts
N, K = [int(x) for x in input().strip().split()]
arr = input().strip().split()

# Now I create an array in which I will store the results
results = []

# I loop through the upvotes array and increase non-increasing and non-decreasing counters if the conditions are met,
# for each window's result (3 consecutive numbers). I then append each window's result to the results array I created
for i in range(len(arr)-2):
    non_inc, non_dec = 0, 0

    if arr[i] >= arr[i+1]: non_inc += 1
    if arr[i] <= arr[i+1]: non_dec +=1

    if arr[i+1] >= arr[i+2]: non_inc += 1
    if arr[i+1] <= arr[i+2]: non_dec +=1

    if non_inc == 2: non_inc += 1
    if non_dec == 2: non_dec += 1

    results.append(non_dec - non_inc)

# I go through each item in the results array and print it
for i in results:
    print(i)


