# https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = []
    win = [6, 6, 5, 4, 3, 2, 1]
    small = 0
    zero = 0
    for i in range(6):
        if win_nums[i] in lottos:
            small += 1
        if lottos[i] == 0:
            zero += 1
    answer.append(win[zero + small])
    answer.append(win[small])
    return answer
