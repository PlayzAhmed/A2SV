# Problem: Swap Cases - https://www.hackerrank.com/challenges/swap-case?isFullScreen=true

def swap_case(s):
    res = ""
    for i in range(len(s)):
        if s[i].islower():
            res += s[i].upper()
        else:
            res += s[i].lower()
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)