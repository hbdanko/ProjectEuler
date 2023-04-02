
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
# For example, 2143 is a 4-digit pandigital and is also prime.
# 
# What is the largest n-digit pandigital prime that exists?

def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    else:
        if number % 2 == 0:
            return False
        else:
            for div in range(3, int(number ** 0.5 + 1), 2):
                if number % div == 0:
                    return False
            else:
                return True

def is_pandigital(number):
    
    number = str(number)
    digits = []
    
    for enum, digit in enumerate(number):
        if digit in number[ : enum]:
            return False
        
        digits.append(int(digit))
        
    pandigital = [digit for digit in range(1, len(number) + 1)]
    
    return pandigital == sorted(digits)

def pandigital_prime(nth):
    ceil = 10 ** 7 + 1
    floor = 10 ** 1
    
    count = 0
    
    for num in range(ceil, floor, - 2):
        if is_prime(num) == True and is_pandigital(num) == True:
            count += 1
            if count == nth:
                return num
        else:
            continue

pandigital_prime(1)