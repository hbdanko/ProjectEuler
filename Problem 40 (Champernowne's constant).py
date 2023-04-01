# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the following expression.

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

def champ_const(wanted_digits):
    fraction = '.'
    num = 1
    digits = []

    while True:
        if len(fraction) > max(wanted_digits):
            for digit in wanted_digits:
                digits.append(int(fraction[digit]))
            break
        else:
            fraction += str(num)
            num += 1

    ans = 1

    for digit in digits:
        ans *= digit

    return ans 

wanted_digits = [1, 10, 100, 1000, 10000, 100000, 1000000]

champ_const(wanted_digits)