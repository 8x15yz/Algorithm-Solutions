# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = []
    cnt = 9999
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0]:
            cnt = i
            break
        elif words[i] in words[:i]:
            cnt = i
            break
    
    if cnt == 9999:
        answer = [0, 0]
    else:
        answer = [cnt%n+1, cnt//n+1]
        
    return answer
