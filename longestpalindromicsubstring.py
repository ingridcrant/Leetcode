"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""

def expand(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    
    return s[(l+1):r]

def longestPalindrome(s):
    longest_string = ""
    
    for i in range(len(s)):
        first = expand(s, i, i)
        if len(first) > len(longest_string):
            longest_string = first
        
        second = expand(s, i, i + 1)
        if len(second) > len(longest_string):
            longest_string = second
        
    return longest_string

# test case
s = "cbbd"
print("The longest palindromic substring is " + '"' + longestPalindrome(s) + '"' + ".")