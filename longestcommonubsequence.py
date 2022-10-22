# -----------PROBLEM--------------

# Given two strings text1 and text2, return the length of their longest common subsequence. 
# If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) 
# deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

# Example 1:
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.

# Example 2:
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.

# Example 3:
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.

# Constraints:

# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.

# -----------SOLUTION-------------

# Approach with Dynamic Programming. Use memoization to avoid timing out with larger testcases.

def lcswithIndices(s1, s2, i, j, dp):
    if (i, j) not in dp:
        if i == len(s1) or j == len(s2):
            # no common subsequence exists with an empty string
            dp[(i, j)] = 0
        elif s1[i] == s2[j]:
            # found a common letter, all that's left to compare is the remainder of the strings
            dp[(i, j)] = 1 + lcswithIndices(s1, s2, i + 1, j + 1, dp)
        else:
            # first letters don't match
            # we want to see if we can find the first letter of one string in the remainder of the other
            #   -> this process is applied recursively to the remaining letters

            # since we want to find the LONGEST common subsequence, we choose the result that gives us the larger count
            dp[(i, j)] = max(
                lcswithIndices(s1, s2, i + 1, j, dp),
                lcswithIndices(s1, s2, i, j + 1, dp))
    
    return dp[(i, j)]

def longestCommonSubsequence(s1, s2):
    dp = {}
    return lcswithIndices(s1, s2, 0, 0, dp)