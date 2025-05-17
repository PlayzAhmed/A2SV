# Problem: Recursively remove all adjacent duplicates - https://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/

s = input()

def remove(s):
    n = len(s)
    new_s = ""

    
    i = 0
    while i < n:
        repeated = False
        while i < n - 1 and s[i] == s[i + 1]:
            repeated = True
            i += 1

        if not repeated:
            new_s += s[i]
        i += 1
    
    if n == len(new_s):
        return new_s
    return remove(new_s)

print(remove(s))