def countSubstrings(s):
    res = 0
    
    for i in range(len(s)):
        res += countPalindromes(s, i, i) + countPalindromes(s, i, i + 1)
    
    return res

def countPalindromes(s, l, r):
    res = 0
    
    while l >= 0 and r < len(s) and s[l] == s[r]:
        res += 1
        l -= 1
        r += 1
    
    return res

# test case
s = "abc"
print("The number of palindromic substrings in " + s + " is " + str(countSubstrings(s)) + ".")