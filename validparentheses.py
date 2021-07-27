def isValid(s):
    open_to_close = {"(":")", "{":"}", "[":"]"}
    to_close_str = ""
    
    for char in s:
        if char in open_to_close:
            to_close_str = open_to_close[char] + to_close_str
        else:
            if to_close_str == "":
                return False
            else:
                if char != to_close_str[0]:
                    return False
                else:
                    to_close_str = to_close_str[1:]
    
    if to_close_str != "":
        return False
    
    return True