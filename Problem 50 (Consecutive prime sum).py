# The prime 41, can be written as the sum of six consecutive primes:
# 
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# 
# The longest sum of consecutive primes below one-thousand that adds to a prime, 
# contains 21 terms, and is equal to 953.
# 
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

def is_prime(number):
    if number == 0:
        return False
    elif number == 1:
        return False
    elif number == 2:
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

def consecutive_prime_sum(limit):
    
    primes = [number for number in range(limit) if is_prime(number) == True]
    last_j = len(primes)
    the_prime = 0
    largest_consecutive_count = 1

    for i in range(len(primes)):
        for j in range(i + largest_consecutive_count, last_j):
            con_sum = sum(primes[i : j])
            if con_sum < limit:
                if con_sum in primes:
                    largest_consecutive_count = j - i
                    the_prime = con_sum
            else:
                last_j = j + 1
                break
                
    return largest_consecutive_count, the_prime

consecutive_prime_sum(1000000)