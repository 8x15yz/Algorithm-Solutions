# https://school.programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    answer = 0
    # 그리디
    # 최대 몇개의 부서에 지원이면 작은 애부터 
    for i in sorted(d):
        if budget < i:
            break
        else:
            budget -= i
            answer += 1
        
    return answer
