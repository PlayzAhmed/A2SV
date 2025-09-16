# Problem: sWapCaSe - https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    diff = 97 - 65
    ans = ""
    
    for x in s:
        if 65 <= ord(x) <= 90:
            ans += chr(ord(x)+diff)
        elif 97 <= ord(x) <= 122:
            ans += chr(ord(x)-diff)
        else:
            ans += x
            
    return ans