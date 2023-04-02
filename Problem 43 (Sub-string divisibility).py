
# The number, 1406357289, is a 0 to 9 pandigital number because 
# it is made up of each of the digits 0 to 9 in some order, 
# but it also has a rather interesting sub-string divisibility property.
# 
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
# 
# d2d3d4=406 is divisible by 2
# 
# d3d4d5=063 is divisible by 3
# 
# d4d5d6=635 is divisible by 5
# 
# d5d6d7=357 is divisible by 7
# 
# d6d7d8=572 is divisible by 11
# 
# d7d8d9=728 is divisible by 13
# 
# d8d9d10=289 is divisible by 17
# 
# Find the sum of all 0 to 9 pandigital numbers with this property.

def is_pandigital(number):
    list_vrsn = [int(num) for num in str(number)]
    
    if len(list_vrsn) != 10:
        return False
    else:
        return len(list_vrsn) == len(set(list_vrsn))

def is_sub_div(number):
    number = str(number)
    primes = [2, 3, 5, 7, 11, 13, 17]
    
    for i in range(1, len(number) - 2):
        if int(number[i : i + 3]) % primes[i - 1] != 0:
            return False
    else:
        return True

def sub_string_divisibity():
    from itertools import permutations
    
    numbers = range(10)
    perms = permutations(numbers)
    ans = 0
    filtered_perms = [perm for perm in perms if perm[0] != 0]
    
    for perm in filtered_perms:
        number = 0
        for enum, digit in enumerate(reversed(perm)):
            number += 10 ** enum * digit
        
        if is_pandigital(number) == True and is_sub_div(number) == True:
            ans += number
            
    return ans

sub_string_divisibity()