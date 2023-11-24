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

# 고친거
def solution(sequence, k):
    answer = []
    mindex = float("inf") 
    minrge = float("inf") 
    l = -1
    for i in range(len(sequence)-1, 0, -1):
        l += 1
        total = 0
        for j in range(0, len(sequence)-l):
            total += sequence[i-j]
            if total == k: 
                if j < minrge and i-j < mindex:
                    minrge, mindex = j, i-j
            elif total > k: break
    return [mindex, mindex+minrge]
