# The number 3797 has an interesting property. 
# Being prime itself, it is possible to continuously remove digits from left to right, 
# and remain prime at each stage: 3797, 797, 97, and 7. 
# Similarly we can work from right to left: 3797, 379, 37, and 3.
# 
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# 
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

def is_prime(number):
    if number in [0, 1]:
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

def is_truncatable(number):
    number = str(number)
    lenght = len(number)
    sub_numbers = []
    
    sub_numbers.extend(int(number[0 : num]) for num in range(1, lenght))
    sub_numbers.extend(int(number[num : lenght]) for num in range(1, lenght))
    
    return all(is_prime(num) for num in sub_numbers)

def truncatable_primes():
    count = 0
    n = 11
    ans = 0
    
    while count < 11:
        if is_prime(n) == True:
            if is_truncatable(n) == True:
                ans += n
                n += 2
                count += 1
            else:
                n += 2
        else:
            n += 2
    
    return ans

truncatable_primes()