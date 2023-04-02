# It was proposed by Christian Goldbach that every odd composite number can be written as 
# the sum of a prime and twice a square.

# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

def is_prime(number):
    if number < 2:
        return False
    if number == 2:
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
            
def is_gold_conj(x):

    for y in range(1, x):
        if is_prime(y) == True:
            z = ((x - y) / 2) ** 0.5
            if z.is_integer() == True:
                return True

    return False

def non_gold_conj():
    number = 9

    while True:
        if is_prime(number) == False and is_gold_conj(number) == False:
            return number
        else:
            number += 2
            continue

non_gold_conj()

