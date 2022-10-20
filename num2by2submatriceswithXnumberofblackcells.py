# Given a matrix with (rols, cols) and an array black, which indicates the cells where the bits are set to one. 
# Identify the number of 2x2 matrices which have 0 bits set to one, 1 bit set to one, 2 bits set to one, 
# 3 bits set to one, 4 bits set to one.

# 1 <= rows <= 10^5
# 1 <= cols <= 10^5
# 0 <= black.length <= 500

# example: rows=3, cols=3, black= [[0,0],[0,1],[1,0]]
# output = [1,2,0,1,0]

# Explanation:
# The given matrix is 
# [
#   1,  1,  0
#    1,  0,  0
#    0,  0,  0
# ]

# there are two 2x2 sub matrices with one bit being set to one
# there is one 2x2 sub matrices with three bits being set to one.
# there is one 2x2 sub matix with 0 bits being set to one
# there are zero 2x2 sub matrices with 2 bits being set, 3 bits being set, 4 bits being set
# Hence output is [1,2,0,1,0]

# Example 2:
# rows = 10000, cols = 10000, black = []
# output = [99980001, 0, 0, 0, 0]

# SOLUTION

# Given that black.length <= 500, there is a maximum of 2000 submatrices that can contain 1, 2, 3, or 4 black bits.
#   to give a visual explanation of this, there is a maximum of 10^5 rows and 10^5 columns.

#   Imagine that we place a black bit on every other bit of the matrix's diagonal. Then we'd alternate through 500 * 2 = 1000 rows and columns,
#       which is still less than the maximum of 10^5 rows and 10^5 columns.

#       [0, 0, 0, 0, 0, ....., 0, 0, 0, ......, 0]
#       [0, 1, 0, 0, 0, ....., 0, 0, 0, ......, 0]
#       [0, 0, 0, 0, 0, ....., 0, 0, 0, ......, 0]
#       [0, 0, 0, 1, 0, ....., 0, 0, 0, ......, 0]
#       [0, 0, 0, 0, 0, ....., 0, 0, 0, ......, 0]
#       [0, 0, 0, 0, 0, ....., 0, 1, 0, ......, 0]
#       [0, 0, 0, 0, 0, ....., 0, 0, 0, ......, 0]

#   Surrounding every black bit, we can create 4 distinct 2x2 submatrices containing just one black bit. 
#   Since all black bits have one row and column between each of them, there are 500 * 4 = 2000 distinct 2x2 submatrices 
#   containing one bit. Logically, the number of 2, 3, and 4 black bit 2x2 submatrices has to be less than the maximum amount 
#   of 1 black bit 2x2 submatrices, 2000.

# Traversing the max 2000 possible black bit submatrices is MUCH more efficient than traversing the max (10^5 - 1) * (10^5 - 1) total 2x2 submatrices.

def solve(rows, cols, black):
    result = [0, 0, 0, 0, 0]

    seenbits = set()    # seenbits stores the top left corners of submatrices we have seen
    blackbits = set(((x, y) for [x, y] in black))   # convert blackbits from list to set for O(1) lookup

    for (x, y) in blackbits:
        # current bit (x, y) can be either be the bottom right, top right, bottom left, or top left bit of the 2x2 submatrix
        for (topleftx, toplefty) in [(x - 1, y - 1), (x - 1, y), (x, y - 1), (x, y)]:
            if (topleftx, toplefty) in seenbits or topleftx < 0 or toplefty < 0 or topleftx >= rows - 1 or toplefty >= cols - 1:
                continue

            seenbits.add((topleftx, toplefty))

            # iterate through all 4 bits in the current 2x2 submatrix and count the black bits
            blackcount = 0
            for dx in range(2):
                for dy in range(2):
                    if (topleftx + dx, toplefty + dy) in blackbits:
                        blackcount += 1
            
            result[blackcount] += 1
    
    # there are (rows - 1) * (cols - 1) total 2x2 submatrices. The number of 0 black bit submatrices is:
    #       total submatrices - 1 black bit submatrices - 2 black bit submatrices - 3 black bit submatrices - 4 black bit submatrices
    result[0] = (rows - 1) * (cols - 1) - sum(result[1:])

    return result

# TEST 1
rows1, cols1 = 3, 3
black1 = [[0,0],[0,1],[1,0]]

# should be [1,2,0,1,0]
print(solve(rows1, cols1, black1))

# TEST 2
rows2, cols2 = 10000, 10000
black2 = []

# should be [99980001, 0, 0, 0, 0]
print(solve(rows2, cols2, black2))
