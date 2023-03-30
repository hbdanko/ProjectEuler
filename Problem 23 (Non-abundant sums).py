# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
# which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant 
# if this sum exceeds n.
# 
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
# the smallest number that can be written as the sum of two abundant numbers is 24. 
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written 
# as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis even though 
# it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# 
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def is_abundant(number):
    div_sum = 0

    for div in range(1, int(number / 2) + 1):
        if number % div == 0:
            div_sum += div

    return div_sum > number

def abundant_numbers(limit):
    ans = []

    for number in range(1, limit + 1):
        if is_abundant(number) == True:
            ans.append(number)

    return ans

def non_abundant_sums(limit):
    abun_nums = abundant_numbers(limit + 1)
    sum_of_abundant_numbers = set()

    for i in range(len(abun_nums)):
        for j in range(i + 1):
            abun_sum = abun_nums[i] + abun_nums[j]
            if abun_sum > limit:
                continue
            else:
                sum_of_abundant_numbers.add(abun_sum)

    ans = 0

    for num in range(limit + 1):
        if num not in sum_of_abundant_numbers:
            ans += num

    return ans

non_abundant_sums(28123)