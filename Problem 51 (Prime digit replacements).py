# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 
# 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, 
# this 5-digit number is the first example having seven primes among the ten generated numbers, 
# yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
# Consequently c, being the first member of this family, is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number 
# (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.


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
            
def number_family(number, family):
    num = str(number)
    num_map = {}

    for enum, digit in enumerate(num):
        num_map[enum] = digit


    for i in range(1, len(num_map)):
        for j in range(i):
            for q in range(j):
                replaced = num_map.copy()
                replaced.update({i : 'x', j : 'x', q : 'x'})
                
                formation = ''.join(replaced.values())

                sub_family = []

                if formation in family:
                    continue
                else:
                    for digit in range(10):
                        member = formation.replace('x', str(digit))
                        
                        if is_prime(int(member)) == False or member[0] == '0':
                            continue
                        else:
                            sub_family.append(int(member))

                    family[formation] = sub_family

    return family

def family_collector():

    family = {}
    current_number = 100

    while True:
        if any(len(arr) > 7 for arr in family.values()) == True:
            return [min(num) for num in family.values() if len(num) > 7]
        else:
            number_family(current_number,family)
            current_number += 1

family_collector()