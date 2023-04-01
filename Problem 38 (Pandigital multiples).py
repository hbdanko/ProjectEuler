# Take the number 192 and multiply it by each of 1, 2, and 3:
# 
# 192 × 1 = 192
# 
# 192 × 2 = 384
# 
# 192 × 3 = 576
# 
# By concatenating each product we get the 1 to 9 pandigital, 192384576. 
# We will call 192384576 the concatenated product of 192 and (1,2,3)
# 
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, 
# giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
# 
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as 
# the concatenated product of an integer with (1,2, ... , n) where n > 1?

def is_pandigital(number):
    list_vrsn = [int(num) for num in str(number)]
    
    if 0 in list_vrsn:
        return False
    else:
        return len(list_vrsn) == len(set(list_vrsn))

def pandigital_multiples(nth):
    n = 1
    product = 1
    concatenated_product = ''
    ans = []
    
    while True:
        concatenated_product += str(n * product)
        if len(concatenated_product) == 9 and is_pandigital(int(concatenated_product)) == True:
            ans.append(int(concatenated_product))
        elif len(concatenated_product) < 9:
            product += 1
            continue
        elif len(str(n)) > 4:
            break
        else:
            n += 1
            product = 1
            concatenated_product = ''
            continue
    
    ans.sort(reverse = True)
    
    return ans[nth - 1]

pandigital_multiples(1)