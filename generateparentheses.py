"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""

def generateParenthesis(n):
    # dynamic programming approach
    dp = [['']] + [[] for _ in range(n)]
    for i in range(n + 1):
        for j in range(i):
            for x in dp[j]:
                for y in dp[i - j - 1]:
                    dp[i].append('(' + x + ')' + y)
    return dp[n]

# test case
n = 5
print(generateParenthesis(n))