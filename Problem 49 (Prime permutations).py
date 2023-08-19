# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, 
# is unusual in two ways: 
# (i) each of the three terms are prime, and, 
# (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
# exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?

from itertools import permutations

#Tests a number is prime or not
def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        if num % 2 == 0:
            return False  
        else:
            for div in range(3, int(num ** 1 / 2), 2):
                if num % div == 0:
                    return False
            else:
                return True

# Returns 4 digit prime numbers in a permutation family of a number
def prime_perms_arr(num):
    perms = {int(''.join(perm)) for perm in permutations(str(num)) if is_prime(int(''.join(perm))) == True and perm[0] != '0'}
    return sorted(perms)

# Returns arithmetic sequence numbers of given prime permutation array if exists
def is_arithmetic_seq(arr):
    for i in range(len(arr) - 2):
        for q in range(i + 1, len(arr)):
            current_number = arr[i]
            next_number = arr[q]
            diff = next_number - current_number
            candidate = next_number + diff

            if candidate in arr:
                return True, [current_number, next_number, candidate]
            
    return False, [current_number, next_number, candidate]

# Returns all numbers that has arithmetic sequence in a list and concatenated versions
def problem_49():
    ans = []
    for num in range(10 ** 3, 10 ** 4):
        if is_prime(num) == True:
            arr = prime_perms_arr(num)
            seq = is_arithmetic_seq(arr)

            if len(arr) > 2 and seq[0] == True:
                if seq[1] in ans:
                    continue
                else:
                    ans.append(seq[1])

    return ans, [int(''.join(map(str, arr))) for arr in ans]

problem_49()
