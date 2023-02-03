#https://school.programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    answer = 0
    for _ in range(500):
        if num == 1:
            break
        elif num%2 == 0:
            num //= 2
            answer += 1
        else:
            num = num*3+1
            answer += 1
    else:
        answer = -1        
    return answer
