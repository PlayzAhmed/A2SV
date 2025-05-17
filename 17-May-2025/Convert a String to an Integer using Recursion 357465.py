# Problem: Convert a String to an Integer using Recursion - https://www.geeksforgeeks.org/convert-a-string-to-an-integer-using-recursion/

num = input()

def stringToInt(num, index):
    if index == 0:
        return int(num[index])
    
    return 10 * stringToInt(num, index - 1) + int(num[index])

def solve(num):
    return stringToInt(num, len(num) - 1)

str_num = solve(num)
print(str_num)