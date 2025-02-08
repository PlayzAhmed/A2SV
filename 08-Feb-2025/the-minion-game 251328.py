# Problem: the-minion-game - https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

def minion_game(string):
    n = len(string)
    v = "AEIOU"
    
    k = 0
    s = 0
    
    for i in range(n):
        if string[i] in v:
            k += n - i
        else:
            s += n - i
            
    if s > k:
        print("Stuart " + str(s))
    elif k > s:
        print("Kevin " + str(k))
    else:
        print("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)