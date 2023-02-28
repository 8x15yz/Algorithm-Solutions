# https://school.programmers.co.kr/learn/courses/30/lessons/70129

# 제출 안되고있는 코드
def solution(s):
    cnt, lev = 0, 0
    while True:
        if s == '1':
            break
        for i in s:
            if i == '0':
                cnt += 1
        else:
            # print(str(bin(len(s)-cnt)[2:]))
            s = str(bin(len(s)-cnt)[2:])
            lev += 1
    answer = [lev, cnt]
    return answer
