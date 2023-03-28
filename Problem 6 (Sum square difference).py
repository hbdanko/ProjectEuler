
# The sum of the squares of the first ten natural numbers is,
# 
# 1 ^ 2 + 2 ^ 2 + ... + 10 ^ 2 = 385
# The square of the sum of the first ten natural numbers is,
# 
# (1 + 2 + ... + 10) ^ 2 = 55 ^ 2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_sq_diff(ceil):

    sum_square = 0
    square_sum = 0

    for number in range(1, ceil + 1):
        square_sum += number
        sum_square += number ** 2

    return (square_sum ** 2) - sum_square

sum_sq_diff(100)






