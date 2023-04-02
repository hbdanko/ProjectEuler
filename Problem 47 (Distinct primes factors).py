# The first two consecutive numbers to have two distinct prime factors are:
# 
# 14 = 2 × 7
# 
# 15 = 3 × 5
# 
# The first three consecutive numbers to have three distinct prime factors are:
# 
# 644 = 2² × 7 × 23
# 
# 645 = 3 × 5 × 43
# 
# 646 = 2 × 17 × 19.
# 
# Find the first four consecutive integers to have four distinct prime factors each. 
# What is the first of these numbers?

def is_prime(number):
    if number == 0:
        return False
    if number == 1:
        return False
    if number == 2:
        return True
    else:
        if number % 2 == 0:
            return False
        else:
            for div in range(3, int(number ** (1 / 2) + 1), 2):
                if number % div == 0:
                    return False
            else:
                return True

def prime_factors(number):
    prime_factor_list = []
    
    if is_prime(number) == True:
        return prime_factor_list
    
    while number % 2 == 0:
        prime_factor_list.append(2)
        number = number / 2
        
    for div in range(3, int(number ** (1 / 2) + 1), 2):
        
        while number % div == 0:
            prime_factor_list.append(div)
            number = number / div
                     
    if number > 2:
        prime_factor_list.append(int(number))
        
    return [num ** prime_factor_list.count(num) for num in set(prime_factor_list)]

def distinct_prime_factors(consecutive_number):
    number = 4
    
    while True:
        if all(len(prime_factors(num)) == consecutive_number for num in range(number, number + consecutive_number)):
            distinct_factors = []
            for num in range(number, number + consecutive_number):
                distinct_factors.extend(prime_factors(num))
                
            if len(distinct_factors) == len(set(distinct_factors)):
                return number
            else:
                number += 1
                continue
        else:
            number += 1
            continue

distinct_prime_factors(4)