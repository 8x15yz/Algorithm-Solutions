# https://school.programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    answer = 0
    three = ''
    id = 0
    while True:
        if n < 3**id:
            break
        else:
            id += 1
            
    for i in range(id-1, -1, -1):
        for j in range(3, -1, -1):
            if (3**i)*j <= n:
                three += str(j)
                n -= (3**i)*j
                break
    for i in range(len(three)-1, -1, -1):
        answer += (3**(i))*int(three[i])
        
    return answer
