# Problem: Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    scores = sorted(set(score for name, score in students))
    second_lowest = scores[1] 

    result = [name for name, score in students if score == second_lowest]
    
    for name in sorted(result):
        print(name)
