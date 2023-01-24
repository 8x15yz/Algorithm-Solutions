# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    id = [[] for _ in range(len(id_list))]
    mail = [[] for _ in range(len(id_list))]
    for s in report:
        id[id_list.index(s[s.index(' ')+1:])].append(s[:s.index(' ')])

    for i in range(len(id)):
        if len(set(id[i])) >= k:
            for s in set(id[i]):
                answer[id_list.index(s)] += 1
    return answer
