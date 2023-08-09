# https://school.programmers.co.kr/learn/courses/30/lessons/159994

def solution(cards1, cards2, goal):
    while goal:
        card = goal.pop(0)
        if cards1 and card == cards1[0]: cards1.pop(0)
        elif cards2 and card == cards2[0]: cards2.pop(0)
        else: return "No"
    return "Yes"
