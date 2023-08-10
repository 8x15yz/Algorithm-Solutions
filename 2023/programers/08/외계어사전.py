# https://school.programmers.co.kr/learn/courses/30/lessons/120869


def solution(spell, dic):
    answer = 0
    # spell, dic =
    for word in dic:
        spelling = {key:0 for key in spell}
        for w in word:
            if w in spell and spelling[w] != 1: spelling[w] = 1 
            else: break
        else: 
            if 0 in spelling.values(): break
            else: return 1
            
    return 2
# 3번테케 ... 뭐임대체
