#https://school.programmers.co.kr/learn/courses/30/lessons/42578 
def solution(clothes):
    # 가짓수만 결과로 내보내면 되니까 연산하기만 하면 되는 쉬운문제였음
    dicty = {}
    for cl in clothes:
        if cl[1] in dicty:
            dicty[cl[1]].append(cl[0])
        else:
            dicty[cl[1]] = [cl[0]]
    arr = [1 for _ in range(len(dicty))]
    ii = 0
    for clo in dicty:
        for c in dicty[clo]:
            print(c)
            arr[ii] += 1
        ii += 1
    answer = 1
    for i in range(len(arr)):
        answer *= arr[i]
    return answer-1
