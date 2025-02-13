# Problem: Python Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

from collections import defaultdict

if __name__ == '__main__':
    
    rec = defaultdict(list)
    grades = set()

    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        rec[score].append(name)
        grades.add(score)
    
    grades = sorted(grades) 
    print("\n".join(sorted(rec[grades[1]])))