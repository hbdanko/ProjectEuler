# 2 ^ 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# 
# What is the sum of the digits of the number 2 ^ 1000?

def power_digit_sum(num, power):
    sum = 0
    
    digits = list(str(num ** power))
    
    for digit in digits:
        sum += int(digit)
        
    return sum

power_digit_sum(2, 1000)
