def lengthOfLongestSubstring(s):
    max_len = 0
    string_so_far = ""
    
    for char in s:
        if char not in string_so_far:
            string_so_far += char
        else:
            max_len = max(max_len, len(string_so_far))
            divide = string_so_far.index(char)
            string_so_far = string_so_far[(divide+1):] + char
    
    max_len = max(max_len, len(string_so_far))
    
    return max_len