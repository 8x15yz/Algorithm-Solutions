#https://school.programmers.co.kr/learn/courses/30/lessons/134240
# 30분
def solution(food):
    answer = ''
    for i in range(1, len(food)):
        if food[i]%2 != 0:
            food[i] -=1
        food[i] = int(food[i]/2)
    print(food)
    for i in range(len(food)-1, 0, -1):
        answer += str(i)*food[i]
    return answer[::-1]+'0'+answer
