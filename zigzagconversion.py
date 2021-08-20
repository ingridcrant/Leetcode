def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    
    row_list = ["" for i in range(numRows)]
    
    curr_row = 0
    direction = 1
    for letter in s:
        row_list[curr_row] = row_list[curr_row] + letter
        curr_row += direction

        if curr_row == 0 or curr_row == numRows - 1:
            direction = (-1)*direction
    
    return "".join(row_list)

# test case
s = "PAYPALISHIRING"
numRows = 3

"""
Zigzag Conversion

P   A   H   N
A P L S I I G
Y   I   R
"""

print(convert(s, numRows))