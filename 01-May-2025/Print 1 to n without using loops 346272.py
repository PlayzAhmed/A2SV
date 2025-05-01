# Problem: Print 1 to n without using loops - https://www.geeksforgeeks.org/print-1-to-n-without-using-loops/

def printNumbers(n):
    if n > 0:
        printNumbers(n - 1)
        print(n)