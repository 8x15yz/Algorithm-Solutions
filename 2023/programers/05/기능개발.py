# https://school.programmers.co.kr/learn/courses/30/lessons/42586


from math import ceil
def solution(progresses, speeds):
    answer = []
    maxDep = 0
    cnt = 1
    for i in range(len(progresses)):
        dep = ceil((100-progresses[i])/speeds[i])
        if maxDep <= dep:
            maxDep = dep
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1
    return answer[1:]+[cnt]
