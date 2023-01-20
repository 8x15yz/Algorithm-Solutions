# https://school.programmers.co.kr/learn/courses/30/lessons/135808

## 시간초과 코드
def solution(k, m, score):
    # 사과최대품질, 포장갯수, 사과들의 점수 배열
    # 사과한상자 가격 = 낮은점수 * m
    answer = 0
    for i in range(len(score)//m):
        answer += min(sorted(score, reverse=True)[(m*i):m*(1+i)])*m
    return answer

  
## 정답코드
## 정렬된 배열(sorted score)을 미리 선언해두고 계산
def solution(k, m, score):
    # 사과최대품질, 포장갯수, 사과들의 점수 배열
    # 사과한상자 가격 = 낮은점수 * m
    stdsc = sorted(score, reverse=True)
    answer = 0
    for i in range(len(score)//m):
        answer += min(stdsc[(m*i):m*(1+i)])*m
    return answer
 
