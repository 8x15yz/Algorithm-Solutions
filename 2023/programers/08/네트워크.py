#https://school.programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    answer = 0
    networks = ["N" for _ in range(len(computers))]
    visit = [0 for _ in range(len(computers))]
    s = 1
    for i in range(len(computers)):
        for j in range(s, len(computers)):
            if computers[i][j]: networks[i] = j
        else: s += 1
    
    print(networks)
    for v in range(len(computers)):
        if visit[v]: continue
        while True:
            if networks[v] == "N":
                answer += 1
                visit[v] = 1
                break
            else: 
                visit[v] = 1
                v = networks[v]
                
    return answer
