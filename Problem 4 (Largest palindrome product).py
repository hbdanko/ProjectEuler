
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        return True

def largest_palindrome(digits):
    largest = 0
    ceil = 10 ** digits
    floor = 10 ** (digits - 1)

    for number1 in range(floor, ceil + 1):
        for number2 in range(floor, number1 + 1):
            product = number1 * number2
            if is_palindrome(product) and product > largest:
                largest = product

    return largest

largest_palindrome(3)

