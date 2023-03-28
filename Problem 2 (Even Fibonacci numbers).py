
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:
# 
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.

def even_fib_sum(limit):
    prev_n = 1
    curr_n = 1
    ans = 0
    
    while curr_n <= limit:
        if curr_n % 2 == 0:
            ans += curr_n
        prev_n, curr_n = curr_n, prev_n + curr_n
    
    return ans

even_fib_sum(4_000_000)