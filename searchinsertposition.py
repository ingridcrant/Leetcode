def binarySearch(sorted_nums, search):
    left_ind = 0
    right_ind = len(sorted_nums) - 1
    middle = (left_ind + right_ind) // 2
    
    while right_ind - left_ind > 1:
        if search == sorted_nums[middle]:
            return middle
        elif search > sorted_nums[middle]:
            left_ind = middle
        elif search < sorted_nums[middle]:
            right_ind = middle
        middle = (left_ind + right_ind) // 2
    
    if search == sorted_nums[left_ind]:
        return left_ind
    elif search == sorted_nums[right_ind]:
        return right_ind
    elif search > sorted_nums[right_ind]:
        return right_ind + 1
    elif search < sorted_nums[left_ind]:
        return left_ind
    else:
        return right_ind
        
def searchInsert(nums, target):
    return binarySearch(nums, target)


# test case
nums = [1,2,3,4,5]
target = 7

print(searchInsert(nums, target))