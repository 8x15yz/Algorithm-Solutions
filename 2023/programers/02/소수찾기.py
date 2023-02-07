#https://school.programmers.co.kr/learn/courses/30/lessons/12921

# 시간초과 오답
def solution(n):
    answer = 0
    for i in range(2, n+1):
        cnt = 0
        for j in range(1, i):
            if i%j == 0:
                cnt += 1
        if cnt == 1:
            answer += 1
            print(i)
    return answer
  
  
# 정답코드
