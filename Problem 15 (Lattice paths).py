# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
# here are exactly 6 routes to the bottom right corner.
# 
# How many such routes are there through a 20×20 grid?

def factorial(num):
    prod = 1
    for i in range(1, num + 1):
        prod *= i
        
    return prod

def lattice_paths(x, y):
    return factorial(x + y) // (factorial(x) * factorial(y))


lattice_paths(20, 20)


