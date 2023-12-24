#https://school.programmers.co.kr/learn/courses/30/lessons/120843

def solution(numbers, k):
    i = 0
    for _ in range(k):
        answer = numbers[i%len(numbers)]
        i += 2
    return answer
