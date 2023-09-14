# https://school.programmers.co.kr/learn/courses/30/lessons/72412

# 시간초과 ..
def solution(information, query):
    answer = []
    for q in query: 
        q = q.replace("and ", "").split()
        cutLine = int(q.pop())
        cnt = 0
        for info in information:
            info = info.split()
            grade = int(info.pop())
            if q == info and cutLine <= grade: cnt += 1
            else:
                for i in range(4):
                    if q[i] not in ("-", info[i]): break
                else:
                    if cutLine <= grade: cnt += 1
        answer.append(cnt)
    return answer
