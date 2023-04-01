# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# 
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# 
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

def factorial(number):
    if number in [0, 1]:
        return 1
    
    ans = 1
    
    for i in range(1, number + 1):
        ans *= i
        
    return ans

def is_digit_factorial(number):
    ans = 0
    
    for digit in str(number):
        ans += factorial(int(digit))
    
    return ans == number

def digit_factorials():
    ans = 0

    for num in range(3, 1000000):
        if is_digit_factorial(num) == True:
            ans += num

    return ans

digit_factorials()