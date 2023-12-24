## https://school.programmers.co.kr/learn/courses/30/lessons/68645

## 푸는중 .. 
dt = [(1, 0), (0, 1), (-1, -1)]
def solution(n):
    answer = []
    arr = [[0 for _ in range(n)] for _ in range(n)]
    eDNum, level, i, j, d = (n**2-n)//2 + n, 2, 0, 0, 0
    arr[0][0] = level
    
   # while level < eDNum + 1:
    for _ in range(23):
        di, dj = i+dt[d][0], j+dt[d][1]
        if 0 <= di < n and 0 <= dj < n:
            if arr[di][di] == 0:
                arr[di][di] = level
                level += 1
                i, j = di, dj
            else: d = (d + 1)%3
        for a in arr: print(a)
        print()
    return answer
