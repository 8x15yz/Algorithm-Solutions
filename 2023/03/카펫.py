#https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    for i in range(1, yellow+1):
        if yellow%i == 0:
            if brown-4 == (yellow//i)*2+i*2:
                answer = [yellow//i+2, i+2]
    return sorted(answer, reverse=True)
