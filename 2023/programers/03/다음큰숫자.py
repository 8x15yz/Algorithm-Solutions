# https://school.programmers.co.kr/learn/courses/30/lessons/12911
# 러프코드
def solution(n):
    answer = 0
    cnt = 0
    for i in bin(n)[2:]:
        if i == 1:
            cnt += 1
    while True:
        n += 1
        ct = 0
        for j in bin(n)[2:]:
            if j == 1:
                ct += 1
        else:
            if ct == cnt:
                answer = n
                break
    return answer
