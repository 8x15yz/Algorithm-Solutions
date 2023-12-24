#https://school.programmers.co.kr/learn/courses/30/lessons/12921

# 시간초과 오답
# 깡으로 브루트포스 돌린 코드
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
  
  
# 시간초과 오답 2
# 소수 배열에 대해 나눠보고 나눠지지 않으면 소수 배열에 수를 추가하는 방식
def solution(n):
    thtn = []
    for i in range(2, n+1):
        for t in thtn:
            if i%t == 0:
                break
        else:
             thtn.append(i)  
    return len(thtn)
