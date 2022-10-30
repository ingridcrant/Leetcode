# -------------PROBLEM---------------

# 2457. Minimum Addition to Make Integer Beautiful

# You are given two positive integers n and target.

# An integer is considered beautiful if the sum of its digits is less than or equal to target.

# Return the minimum non-negative integer x such that n + x is beautiful. The input will be 
# generated such that it is always possible to make n beautiful.

# Example 1:

# Input: n = 16, target = 6
# Output: 4
# Explanation: Initially n is 16 and its digit sum is 1 + 6 = 7. After adding 4, n becomes 20 and 
# digit sum becomes 2 + 0 = 2. It can be shown that we can not make n beautiful with adding 
# non-negative integer less than 4.
# Example 2:

# Input: n = 467, target = 6
# Output: 33
# Explanation: Initially n is 467 and its digit sum is 4 + 6 + 7 = 17. After adding 33, n becomes 
# 500 and digit sum becomes 5 + 0 + 0 = 5. It can be shown that we can not make n beautiful with 
# adding non-negative integer less than 33.
# Example 3:

# Input: n = 1, target = 1
# Output: 0
# Explanation: Initially n is 1 and its digit sum is 1, which is already smaller than or equal to target.
 

# Constraints:

# 1 <= n <= 1012
# 1 <= target <= 150
# The input will be generated such that it is always possible to make n beautiful.

# -------------SOLUTION---------------

# Start from last index. If sum of the digits is over target:
#   - Incrementing the digit to 1-9 will just increase sum of digits -> no point if we're trying to decrease the sum
#   - Instead, carry to the next digit (add 10 - currdigit to currdigit)
#       - resets the current digit to 0
#       - increments the next digit by 1
#     The net difference in sum digits is 1 - currdigit (which is <= 0) so it reduces sum digits
# Restart the procedure until sum of the digits is under or equal to target

def makeIntegerBeautiful(n: int, target: int) -> int:
    oldn = n
    
    # seperates n into its digits, adding a 0 in front (in case we have to carry n's first digit)
    nseperated = []
    while n > 0:
        nseperated = [n % 10] + nseperated
        n = n // 10
    nseperated = [0] + nseperated
    
    sumdigits = sum(nseperated)
    ind = len(nseperated) - 1
    
    while sumdigits > target:
        # carrying to next digit
        sumdigits -= nseperated[ind]
        sumdigits += 1
        nseperated[ind] = 0
        nseperated[ind - 1] += 1
        ind -= 1
    
    # convert nseperated back into an integer
    s = 0
    exp = 0
    for i in range(len(nseperated) - 1, -1, -1):
        s += nseperated[i] * (10 ** exp)
        exp += 1
    
    # returns the difference between the "beautiful integer" and n
    return (s - oldn)

# Example 1
# n = 16, target = 6
# Output: 4
print(makeIntegerBeautiful(16, 6))

# Example 2
# Input: n = 467, target = 6
# Output: 33
print(makeIntegerBeautiful(467, 6))

# Example 2
# Input: n = 1, target = 1
# Output: 0
print(makeIntegerBeautiful(1, 1))