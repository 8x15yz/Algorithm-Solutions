# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    answer = ''
    cnt = [0 for _ in range(len(completion))]
    for par in participant:
        if par not in completion:
            answer = par
            break
        cnt[completion.index(par)] += 1
    else:
        answer = completion[cnt.index(2)]
    return answer
