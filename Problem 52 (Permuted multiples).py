# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, 
# but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

def is_same_digits(arr):
    str_arr = [''.join(sorted(str(num))) for num in arr]
    return all(item == str_arr[0] for item in str_arr)

def permu_multi(multiples):

    number = 1

    while True:
        arr = [number * multi for multi in multiples]
        if is_same_digits(arr) == True:
            return number
        else:
            number += 1

multiples = [1, 2, 3, 4, 5, 6]

permu_multi(multiples)