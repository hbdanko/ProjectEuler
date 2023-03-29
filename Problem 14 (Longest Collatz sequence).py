# The following iterative sequence is defined for the set of positive integers:
# 
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# 
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.

def collatz_seq(num):
    
    counter = 1
    
    while num > 1:
        if num % 2 == 0:
            num = num / 2
            counter += 1
        else:
            num = 3 * num + 1
            counter += 1
    
    return counter

def longest_collatz_sequence(ceiling_number):
    
    largest_number = 0
    largest_count = 0
    
    for i in range(ceiling_number, 1, -1):
        if collatz_seq(i) > largest_count:
            largest_number = i
            largest_count = collatz_seq(i)
    
    return largest_number

longest_collatz_sequence(1000000)