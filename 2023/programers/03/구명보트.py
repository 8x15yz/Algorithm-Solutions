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
