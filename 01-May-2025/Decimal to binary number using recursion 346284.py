# Problem: Decimal to binary number using recursion - https://www.geeksforgeeks.org/decimal-binary-number-using-recursion/

def convertToBinary(d):
    return str(d % 2) + (convertToBinary(d//2) if d > 1 else '')