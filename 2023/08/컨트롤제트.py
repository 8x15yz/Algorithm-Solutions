# https://school.programmers.co.kr/learn/courses/30/lessons/120853
def solution(s):
    answer = []
    for letter in list(s.split()):
        if letter == "Z":
            answer.pop()
        else:
            answer.append(int(letter))
    return sum(answer)
