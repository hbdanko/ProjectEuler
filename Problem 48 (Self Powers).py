# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# 
# Find the last ten digits of the series,1^1 + 2^2 + 3^3 + ... + 10001000.

def self_powers(limit):
    sum = 0
    
    for num in range(1, limit + 1):
        sum += num ** num
        
    return str(sum)[-10:]

self_powers(1000)