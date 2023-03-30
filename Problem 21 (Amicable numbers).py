# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair 
# and each of a and b are called amicable numbers.
# 
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# 
# Evaluate the sum of all the amicable numbers under 10000.

def divisors_sum(number):
    
    divisors_sum = 1
    
    if number % 2 != 0:
        for i in range(3, number // 2 + 1, 2):
            if number % i == 0:
                divisors_sum += i
    else:
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                divisors_sum += i
                
    return divisors_sum

def amicable_numbers(limit):
    numbers = 0
    
    for i in range(2, limit + 1):
        if i == divisors_sum(divisors_sum(i)) and i != divisors_sum(i):
            numbers += i
        else:
            continue
            
    return numbers

amicable_numbers(10000)