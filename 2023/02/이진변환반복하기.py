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


# 정신이 나간거임 지금 ㅁ니쳣나
# 
def solution(s):
    cntd, lev = 0, 0
    while True:
        cnt = 0
        if s == '1':
            break
        for i in s:
            if i == '0':
                cnt += 1
        else:
            s = bin(len(s)-cnt)[2:]
            lev += 1
            cntd += cnt
            
    answer = [lev, cntd]
    return answer
