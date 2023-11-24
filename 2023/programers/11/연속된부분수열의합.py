# https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    answer = []
    for i in range(len(sequence), 0, -1):
        for j in range(1, len(sequence)+1):
            cut = sequence[i-j:i]
            if cut != []:
                if sum(cut) == k:
                    answer.append([i-j, i-1])
    print(answer)
    return answer
