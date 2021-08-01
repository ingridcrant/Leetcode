def maxArea(heights):
    l = 0
    r = len(heights) - 1
    area = 0
    
    while l < r:
        area = max(area, min(heights[l], heights[r]) * (r - l))
        
        # the shorter wall is keeping the water area small
        # it shouldn't be considered anymore since the width is only getting smaller
        # meaning that we would only get a smaller area by keeping the smaller wall
        # consider the next wall in as it could be higher, and thus result in a larger area
        if heights[l] <= heights[r]:
            l += 1
        else:
            r -= 1
    
    return area

# test case
heights = [1,8,6,2,5,4,8,3,7]
print("max area of water in this container is", maxArea(heights))