
# The number, 197, is called a circular prime because all rotations of the digits: 
# 197, 971, and 719, are themselves prime.
# 
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# 
# How many circular primes are there below one million?

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
        
def is_circular_prime(number):
    
    number = str(number)
    
    circular_numbers = []
    
    for i in range(len(number) - 1):
        number = number[1 : ] + number[0]
        circular_numbers.append(int(number))
        
    return all(is_prime(num) for num in circular_numbers)

def circular_primes(ceil):
    ans = 1
    
    for num in range(3, ceil + 1, 2):
        if is_prime(num) == False:
            continue
        else:
            if is_circular_prime(num) == False:
                continue
            else:
                ans += 1
                
    return ans

circular_primes(1_000_000)