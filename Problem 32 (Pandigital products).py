# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, 
# containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as 
# a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

def is_product_pandigital(multiplicand, multiplier, product):
     candidate = ''.join(sorted(str(multiplicand) + str(multiplier) + str(product)))

     return candidate == '123456789'

def pandigital_products():
     products = set()

     for multiplicand in range(9999):
          for multiplier in range(multiplicand):
               product = multiplicand * multiplier
               if is_product_pandigital(multiplicand, multiplier, product) == True:
                    products.add(product)
               else:
                    continue

     return sum(products)

pandigital_products()