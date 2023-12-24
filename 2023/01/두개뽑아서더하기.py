# https://school.programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)-1, i, -1):
            if numbers[i] + numbers[j] not in answer:
                answer.append(numbers[i] + numbers[j])
    return sorted(answer)
