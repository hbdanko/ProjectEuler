# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
# there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?

def is_right_triangle(a, b, c):
    return a ** 2 + b ** 2 == c ** 2

def right_triangles(ceil):

    triangles = {}

    for a in range(1, ceil + 1):
        for b in range(1, a + 1):
            c = int((a ** 2 + b ** 2) ** 0.5)
            edge_sum = a + b + c
            if is_right_triangle(a, b, c) == True and edge_sum <= ceil:
                if edge_sum in triangles:
                    triangles[edge_sum].append((a, b, c))
                else:
                    triangles[edge_sum] = [(a, b, c)]

    return triangles

def max_triangles(ceil):

    triangles = right_triangles(ceil)
    count = 0
    ans = 0

    for edge_sum in triangles:
        if len(triangles[edge_sum]) > count:
            count = len(triangles[edge_sum])
            ans = edge_sum

    return ans

max_triangles(1000)