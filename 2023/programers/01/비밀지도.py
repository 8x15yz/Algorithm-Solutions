# 인덱스가 헷갈려서 헤맴
# https://school.programmers.co.kr/learn/courses/30/lessons/17681
def solution(n, arr1, arr2):
    answer = [list(' '*n) for _ in range(n)]
    digit = 0
    # 이진수 변환하고 배열으로 맞추기
    for num in range(n):
        digit = arr1[num]
        for i in range(n-1, -1, -1):
            if digit >= 2**i:
                digit -= 2**i
                answer[num][n-1-i] = '#'
        digit = arr2[num]
        for i in range(n-1, -1, -1):
            if digit >= 2**i:
                digit -= 2**i
                answer[num][n-1-i] = '#'

    for i in range(n):
        answer[i] = ''.join(answer[i])
    return answer
