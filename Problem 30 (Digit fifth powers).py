# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
# 
# - 1634 = 1 ^ 4 + 6 ^ 4 + 3 ^ 4 + 4 ^ 4
# - 8208 = 8 ^ 4 + 2 ^ 4 + 0 ^ 4 + 8 ^ 4
# - 9474 = 9 ^ 4 + 4 ^ 4 + 7 ^ 4 + 4 ^ 4
# 
# As 1 = 1 ^ 4 is not a sum it is not included.
# 
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# 
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def number_power(number, power):
    sum = 0
    for i in str(number):
        sum += int(i) ** power
        
    if sum == number:
        return True
    else:
        return False

def digit_powers(power):
    sum = 0
    
    for number in range(2, power * 9 ** power + 1):
        if number_power(number, power) == True:
            sum += number
            
    return sum

digit_powers(5)




