# https://school.programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        ans = []
        for k in range(len(arr2[0])):
            part = 0
            for j in range(len(arr2)):
                part += (arr1[i][j]*arr2[j][k])
            ans.append(part)
        answer.append(ans)
    
    return answer
