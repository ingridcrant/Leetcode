"""
You are playing a game involving a circular array of non-zero integers nums. Each nums[i] denotes the number of indices forward/backward you must move if you are located at index i:

If nums[i] is positive, move nums[i] steps forward, and
If nums[i] is negative, move nums[i] steps backward.
Since the array is circular, you may assume that moving forward from the last element puts you on the first element, and moving backwards from the first element puts you on the last element.

A cycle in the array consists of a sequence of indices seq of length k where:

Following the movement rules above results in the repeating index sequence seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
Every nums[seq[j]] is either all positive or all negative.
k > 1

Return true if there is a cycle in nums, or false otherwise.

Constraints:
    1 <= nums.length <= 5000
    -1000 <= nums[i] <= 1000
    nums[i] != 0
"""

def circularArrayLoop(nums):
    n = len(nums)
    if n < 2:
        return False
    
    for i in range(n):           
        if nums[i] > 1001: # already visited
            continue
        if nums[i] % n == 0: # makes a self-loop
            continue
        
        original_num = nums[i]
        
        mark = 1001 + i

        # original_num * nums[i] > 0 is true only if original_num and nums[i] are the same sign
        while nums[i] <= 1000 and original_num * nums[i] > 0 and nums[i] % n != 0:
            jump = nums[i]
            nums[i] = mark
            i = (i + jump) % n
            
        if nums[i] == mark:
            return True
        
    return False

# test case
nums = [2,-1,1,2,2]
is_cycle = circularArrayLoop(nums)

if is_cycle:
    print("There is a cycle.")
else:
    print("There is not a cycle.")