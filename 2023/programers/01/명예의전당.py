# https://school.programmers.co.kr/learn/courses/30/lessons/138477
# 1시간

def solution(k, score):
    answer = []
    rank = []
    for i in score:
        rank.append(i)
        rank = sorted(rank, reverse=True)
        if len(rank) < k:
            answer.append(rank[-1])
        else:
            answer.append(rank[k-1])
            
    return answer
