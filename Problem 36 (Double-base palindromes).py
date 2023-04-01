# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

def num_to_binary(number):  
    binary = ''

    while number > 0 :
        binary = str(number % 2) + binary
        number //= 2

    return binary

def is_palindrome(number):
    if str(number)[-1] == '0':
        return False
    
    return str(number) == str(number)[ : : -1]

def sum_palindrome_bases(limit):

    ans = 0

    for number in range(limit + 1):
        binary = num_to_binary(number)

        if is_palindrome(number) == True and is_palindrome(binary) == True:
            ans += number

    return ans

sum_palindrome_bases(1_000_000)