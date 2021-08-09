# rec1 and rec2 are in the format [x1, y1, x2, y2]
def isRectangleOverlap(rec1, rec2):
    return rec1[0] < rec2[2] and rec2[0] < rec1[2] and rec1[1] < rec2[3] and rec2[1] < rec1[3]

# test case
rec1 = [0,0,1,1]
rec2 = [1,0,2,1]
print(isRectangleOverlap(rec1, rec2))