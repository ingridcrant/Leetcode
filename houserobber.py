# House Robber I

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of 
# money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have 
# security systems connected and it will automatically contact the police if two adjacent houses were 
# broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount 
# of money you can rob tonight without alerting the police.

def houserobber1(nums):
    lennums = len(nums)

    # dynamic programing solution, for every house at index i, dp[i + 3] stores its optimal solution
    dp = [0] * (lennums + 3)
    maxsofar = 0
    
    for i in range(lennums):
        # makes the decision of robbing the 2nd last or 3rd last house (whichever one is richer)
        #   don't need to consider houses 4th, 5th, .., nth last since they are already considered in 
        #   robbing 2nd and 3rd last houses
        dp[i + 3] = max(dp[i + 1] + nums[i], dp[i] + nums[i])
        maxsofar = max(maxsofar, dp[i + 3])
    
    return maxsofar

# House Robber II

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of 
# money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor 
# of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically 
# contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of 
# money you can rob tonight without alerting the police.

def houserobber2(nums):
    if len(nums) == 1:
        return nums[0]
    
    # in a circular arrangement, the first and last houses can't be considered together
    #   we can't guarantee this unless we seperate them:
    #       Case 1: houses 0 to n-1 are robbed
    #       Case 2: houses 1 to n are robbed
    # the optimal solution will be the max of both cases
    return max(houserobber1(nums[1:]), houserobber1(nums[:(-1)]))
