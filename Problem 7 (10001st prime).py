
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?

def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    else:
        if number % 2 == 0:
            return True
        else:
            for div in range(3, int(number ** 0.5 + 1), 2):
                if number % div == 0:
                    return False
            else:
                return True
            
            
def nth_prime(n):
    count = 1
    number = 3

    if n == 1:
        return 2
    else:
        while True:
            if is_prime(number) == True:
                count += 1
                if count == n:
                    return number
                else:
                    number += 2
            else:
                number += 2


nth_prime(10001)




