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
def solution(participant, completion):
    answer = ''
    part = {}
    for c in completion:
        if c in part:
            part[c][1] += 1
        else:
            part[c] = [0, 1]
        
    for pt in participant:
        if pt in part:
            part[pt][0] += 1
        else:
            answer = pt
            break
    else:
        for pt in part:
            if part[pt][1]/part[pt][0] < 1:
                answer = pt
            
    return answer

# 설명:
# 분자 = 완료한사람 수
# 분모 = 참가한사람 수
# 분수로 나타내서 1보다 작으면 동명이인 모두 못 들어왔다는 얘기라서 그 이름을 answer 로 
