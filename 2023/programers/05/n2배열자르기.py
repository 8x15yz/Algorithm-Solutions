# https://school.programmers.co.kr/learn/courses/30/lessons/87390
# 시간초과되는코드

def solution(n, left, right):
    answer = []
    for i in range(1, n+1):
        ans = []
        for j in range(1, n+1):
            ans.append(max(i, j))
        answer.append(ans)
    newans = []
    for a in answer:
        newans += a
    return newans[left:right+1]



# 시간초과 ...
def solution(n, left, right):
    answer = []
    endPoint = (right//n+1, right%n+1)
    for i in range(1, n+1):
        for j in range(1, n+1):
            answer+= [max(i, j)]
            if (i, j) == endPoint: 
                return answer[left:]
            

# 이거였엌ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ  아놔 ~
def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        answer.append(max(i//n+1, i%n+1))
    return answer
            
