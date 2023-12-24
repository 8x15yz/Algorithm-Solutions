# https://school.programmers.co.kr/learn/courses/30/lessons/12924
# 당연히틀리죠?
def solution(n):
    answer = 0
    for i in range(n):
        su = 0
        for j in range(i, n+1):
            su += j
            if su == n:
                answer += 1
                break
            elif su > n:
                break
                
    return answer


# 비슷한 코드인것같은데 
def solution(n):
    count = 1
    for j in range(1,n):
        m1 = j
        while True:
            if j == n:
                count += 1
                break
            elif j > n:
                break
            m1 += 1
            j += m1

    return count
