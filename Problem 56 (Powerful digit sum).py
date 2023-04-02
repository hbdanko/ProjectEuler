# A googol (10100) is a massive number: one followed by one-hundred zeros; 
# 100100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

def power_digit_sum(ceil):
    max_sum = 0

    for num1 in range(1, ceil + 1):
        for num2 in range(1, num1 + 1):
            power = num1 ** num2
            digit_sum = sum([int(digit) for digit in str(power)])
            if digit_sum > max_sum:
                max_sum = digit_sum

    return max_sum

power_digit_sum(100)