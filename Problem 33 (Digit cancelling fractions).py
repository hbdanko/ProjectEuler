# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to 
# simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# 
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# 
# There are exactly four non-trivial examples of this type of fraction, 
# less than one in value, and containing two digits in the numerator and denominator.
# 
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

def is_digit_cancellable_fraction(numerator, denominator):
    
    fraction = numerator / denominator
    numerator = str(numerator)
    denominator = str(denominator)
        
    if numerator[1] == denominator[0]:
        digit_cancelled_fraction = int(numerator[0]) / int(denominator[1])
    else:
        return False
        
    return fraction == digit_cancelled_fraction

def digit_cancelling_fractions():
    
    fractions = []
    
    for denominator in range(11, 100):
        for numerator in range(11, denominator):
            if denominator % 10 == 0:
                continue
            else:
                if is_digit_cancellable_fraction(numerator, denominator) == True:
                    fractions.append([numerator, denominator])
    return fractions

def fraction_simplifier(numerator, denominator):
    
    gcd = 1
    smaller = min(abs(numerator), abs(denominator))
    
    for div in range(2, smaller + 1):
        if numerator % div == 0 and denominator % div == 0:
            gcd = div
            
    return int(numerator / gcd), int(denominator / gcd)

def lowest_denominator(fractions):
    numerator = 1
    denominator = 1
    
    for i in (fractions):
        numerator *= i[0]
        denominator *= i[1]
        
    return fraction_simplifier(numerator, denominator)

lowest_denominator(digit_cancelling_fractions())