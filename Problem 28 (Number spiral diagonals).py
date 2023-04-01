# Starting with the number 1 and moving to the right in a 
# clockwise direction a 5 by 5 spiral is formed as follows:
# 
# 21 22 23 24 25
# 
# 20 7  8  9 10
# 
# 19  6  1  2 11
# 
# 18  5  4  3 12
# 
# 17 16 15 14 13
# 
# It can be verified that the sum of the numbers on the diagonals is 101.
# 
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

def spiral_diagonals(axis):
    ceil = axis ** 2
    num = 3
    count = 1
    skip = 2
    ans = 1

    while ceil + 1 > num:
        ans += num
        if count == 4:
            count = 1
            skip += 2
            num += skip
        else:
            num += skip
            count += 1

    return ans

spiral_diagonals(1001)

