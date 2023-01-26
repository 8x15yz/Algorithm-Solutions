#https://school.programmers.co.kr/learn/courses/30/lessons/42748
#4 분만에풂레전드 ~
def solution(array, commands):
    answer = []
    for com in commands:
        answer.append(sorted(array[com[0]-1:com[1]])[com[2]-1])
    return answer
