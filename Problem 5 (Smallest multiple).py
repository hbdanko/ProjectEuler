# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def is_div(num):
    for i in range(11, 21):
        if num % i != 0:
           return False
    else:
        return True


def smallest_multiple(limit):
    num = 2
    
    while True:
        if is_div(num) == False:
            num += 2
        else:
            return num


smallest_multiple(20)



