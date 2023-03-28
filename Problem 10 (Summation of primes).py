# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.


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

def prime_sum(limit):
    ans = 2

    if limit == 2:
        return ans
    else:
        for number in range(3, limit, 2):
            if is_prime(number) == True:
                ans += number

    return ans


prime_sum(2000000)



