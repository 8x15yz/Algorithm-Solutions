# https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(A,B):
    answer = 0
    # 이거 dp인가?
    # 아니다
    A = sorted(A)
    B = sorted(B, reverse=True)
    for i in range(len(A)):
        answer += A[i]*B[i]
    return answer
