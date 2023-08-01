#https://school.programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    answer = 1
    networks = {i:0 for i in range(len(computers))}
    s = 1
    for i in range(len(computers)):
        for j in range(s, len(computers)):
            if computers[i][j]:
                networks[i], networks[j] = 1, 1
        else: s += 1
        
    state = networks[0]
    for i in range(len(computers)):
        if networks[i] != state: answer += 1
        
    return answer
