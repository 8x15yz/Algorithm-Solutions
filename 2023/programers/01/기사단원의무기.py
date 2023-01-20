#https://school.programmers.co.kr/learn/courses/30/lessons/136798
# 

## 시간초과 코드
def solution(number, limit, power):
    #기사 수, 공격력 제한수치, 사용할 무기의 공격력
    answer = 0
    for i in range(1, number+1):
        cnt = 0
        for j in range(1, i+1):
            if i%j == 0:
                cnt += 1
        if cnt> limit:
            answer += power
        else:
            answer += cnt
    return answer
 
## 정답코드
## 약수가 각자 짝이 있다
import math
def solution(number, limit, power):             
    #기사 수, 공격력 제한수치, 사용할 무기의 공격력
    answer = 0
    for i in range(1, number+1):                 
    # 1부터 number 까지의 기사에 대한 약수를 구해야됨
        cnt = 0
        for j in range(1, math.ceil(i**0.5)):  
        # 약수 구하는 프로세스 : 루트값을 중심으로 절반만 카운트해서 *2 하기 
            if i%j == 0:                         
            # 나눠 떨어지면 1을 더하기
                cnt += 1
        if int(i**0.5) == math.ceil(i**0.5):     
        # 약수 중에 제곱근이 있으면 
            cnt = cnt*2 + 1
        else:
            cnt = cnt*2
        if cnt > limit:
            answer += power
        else:
            answer += cnt
            
    return answer
