def generate(numRows):
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1],[1,1]]
    else:
        remain = numRows - 2
        pascal = [[1],[1,1]]
        
        for row in range(remain):
            new_row = [1]
            for num in range(0, len(pascal[-1])-1):
                new_row.append(pascal[-1][num]+pascal[-1][num+1])
            new_row.append(1)
            pascal.append(new_row)
        
        return pascal