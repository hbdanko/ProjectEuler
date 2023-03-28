# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
# a ^ 2 + b ^ 2 = c ^ 2
# For example, 3 ^ 2 + 4 ^ 2 = 9 + 16 = 25 = 5 ^ 2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def pythagorean_triplet(limit):
    for a in range(1, limit):
        for b in range(1, limit):
            c = limit - b - a
            if (a ** 2 + b ** 2) == c ** 2:
                return a * b * c

pythagorean_triplet(1000)
