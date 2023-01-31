# https://school.programmers.co.kr/learn/courses/30/lessons/42576

# 틀린코드
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


# 해시함수로 구현했는데 틀림
def solution(participant, completion):
    answer = ''
    part = {}
    for c in completion:
        part[c] = 0
    for pt in participant:
        if pt in part:
            part[pt] += 1
        else:
            answer = pt
            break
    else:
        for pt in part:
            if part[pt] == 2:
                answer = pt
                break
    return answer

# 정답코드
