# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?

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
            
def largest_prime_factor(number):
    ans = 0

    for div in range(3, int(number ** 0.5 + 1), 2):
        if is_prime(div) == True and number % div == 0:
            ans = div

    return ans
    
largest_prime_factor(600851475143)