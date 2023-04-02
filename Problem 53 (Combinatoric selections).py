# There are exactly ten ways of selecting three from five, 12345:
# 
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

# How many, not necessarily distinct, values of (n r) for 1 ≤ n ≤ 100, are greater than one-million?

def factorial(number):
    ans = 1
    
    for num in range(1, number + 1):
        ans *= num
    
    return ans

def combinatorics(n, r):
    return int(factorial(n) / (factorial(r) * factorial(n - r)))

def combinatorics_selection(n_limit, ans_floor):
    
    count = 0
    
    for n in range(1, n_limit + 1):
        for r in range(1, n):
            if combinatorics(n, r) > ans_floor:
                count += 1
                
    return count

combinatorics_selection(100, 10 ** 6)