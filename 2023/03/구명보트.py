# https://school.programmers.co.kr/learn/courses/30/lessons/42885


# 30점짜리 답 ..
def solution(people, limit):
    answer = 1
    people = sorted(people, reverse=True)
    weight = 0
    while people:
        wait = people.pop()
        if weight + wait > limit:
            answer += 1
            weight = wait
        elif weight + wait == limit:
            answer += 1
            weight = 0
        else:
            weight += wait
    return answer


# ㅠㅠㅠ 틀린답
def solution(people, limit):
    answer = 1
    people = sorted(people, reverse=True)
    weight = 0
    cnt = 0
    while people:
        if cnt <= 1:
            wait = people.pop()
            cnt += 1
            if weight + wait == limit:
                cnt = 0
                weight = 0
                answer += 1
            elif weight + wait > limit:
                ant = 0
                weight = wait
                answer += 1
            else:
                weight += wait
        else:
            # print(cnt)
            cnt = 0
    return answer

# 지독하네 .. 인덱스 접근으로 풀어봤는데 틀림
def solution(people, limit):
    answer = 0
    people = sorted(people, reverse=True)
    i = 0
    cnt, weight = 0, 0
    # a+b > limit => a만 내보내고 index를 b에 포커스 / cnt,weight 초기화 
    # a+b < limit => a, b 둘 다 내보내고 index를 b+1에 포커스 / cnt,weight 초기화 
    while i < len(people):
        if i+1 < len(people) and people[i]+people[i+1] > limit:
            i += 1
            answer += 1
        elif i+1 < len(people) and people[i]+people[i+1] <= limit:
            i += 2
            answer += 1
        else:
            answer += 1
            break
            
    return answer


# 이거는 완전 투포인터 문제였음
# 일단 내가 코드참고해서 푼거
from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    while people:
        if len(people) == 1:
            answer += 1
            break
        elif people[0]+people[-1] <= limit:
            answer += 1
            people.pop()
            people.popleft()
        else:
            answer += 1
            people.pop()
    return answer


# 투퐇인터 코드
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer
