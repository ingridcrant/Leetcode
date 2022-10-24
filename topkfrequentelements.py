# ------------PROBLEM---------------

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# ------------SOLUTION---------------

# Doing some preprocessing steps, we can get the time complexity down to O(n)

# 1. Collect the frequency of each number in nums - O(n)
#   -> store this in a hashmap

# 2. Collect all frequencies - O(n)
#   -> store numbers associated to frequency in a hashmap

# 3. Iterate down from max frequency, len(nums), to min frequency, 1, accumulating the associated numbers - O(n)
#   -> stop when we've accumulated k numbers
#       -> this is the answer!

def topKFrequent(nums, k):
    numstocounts = {}
    for num in nums:
        if num not in numstocounts:
            numstocounts[num] = 1
        else:
            numstocounts[num] += 1
    
    countstonums = {}
    for num in numstocounts.keys():
        if numstocounts[num] not in countstonums:
            countstonums[numstocounts[num]] = [num]
        else:
            countstonums[numstocounts[num]] += [num]
    
    kfrequentels = []
    elcount = 0
    for count in range(len(nums), 0, -1):
        if elcount == k:
            break
        if count in countstonums:
            kfrequentels += countstonums[count]
            elcount += len(countstonums[count])
    
    return kfrequentels