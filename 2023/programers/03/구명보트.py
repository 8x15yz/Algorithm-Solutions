# https://school.programmers.co.kr/learn/courses/30/lessons/42885


def solution(people, limit):
    answer = 1
    people = sorted(people, reverse=True)
    weight = 0
    while people:
        wait = people.pop()
        if weight + wait > limit:
            answer += 1
            weight = wait
        else:
            weight += wait
    return answer
