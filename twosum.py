# python implementation of two sum problem on leetcode
# num -> list of integers
# target -> integer

def twoSum(nums, target):
    for x in range(len(nums)):
        y = target-nums[x]
        if y in nums:
            ind = nums.index(y)
            if x != ind:
                return [x,ind]