# n! means n × (n − 1) × ... × 3 × 2 × 1
# 
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# 
# Find the sum of the digits in the number 100!

def factorial(num):
    prod = 1
    for i in range(1, num + 1):
        prod *= i
        
    return prod

def factorial_digit_sum(number):
    
    factor = factorial(number)
    
    sum = 0
    
    for digit in str(factor):
        sum += int(digit)
        
    return sum

factorial_digit_sum(100)