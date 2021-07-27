def removeDuplicates(nums):
    i = 0
    j = 1
    
    while j < len(nums):
        if nums[i] < nums[j]:
            i += 1
            
            if j > i:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
            
            j += 1
        else:
            j += 1
    
    return nums[:(i+1)]

# test case
arr = [4,4,9,10,10,10,16,90,91,91,91,91,100]
removed_arr = removeDuplicates(arr)
print(removed_arr)