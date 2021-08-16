"""
You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.
"""

def maxOperations(nums, k):
    num_map = {}
    count = 0
    
    for num in nums:
        if num not in num_map:
            num_map[num] = 1
        else:
            num_map[num] = num_map[num] + 1
    
    for num in num_map:
        if num == k-num:
            num_pairs = num_map[num] // 2
            num_map[num] = 0
            count += num_pairs
        elif k-num in num_map:
            num_pairs = min(num_map[num], num_map[k-num])
            num_map[num] = 0
            num_map[k-num] = 0
            count += num_pairs
    
    return count