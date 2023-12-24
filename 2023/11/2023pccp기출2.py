# https://school.programmers.co.kr/learn/courses/30/lessons/250136

v = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def solution(land):
    w, h = len(land[0]), len(land)
    visit = [[0 for _ in range(w)] for _ in range(h)]
    res = []
    for i in range(h):
        for j in range(w):
            if visit[i][j] == 0:
                visit[i][j] = 1
                queue = [(i, j)]
                minW, maxW = w+1, -1
                cnt = 0
                while queue:
                    si, sj = queue.pop(0)
                    for vi, vj in v:
                        ni, nj = si+vi, sj+vj
                        if 0 <= ni < h and 0 <= nj < w and visit[ni][nj] != 2 and land[ni][nj] == 1:
                            queue.append((ni, nj))
                            visit[ni][nj] = 2
                            minW = minW if minW < nj else nj
                            maxW = maxW if maxW > nj else nj
                            cnt += 1
                if cnt != 0:
                    res.append((cnt, minW, maxW))
    answer = 0    
    for i in range(w):
        total = 0
        for cnt, minW, maxW in res:
            if minW <= i <= maxW:
                total += cnt
        answer = max(answer, total)
                
    return answer


## 시간 줄이려고 ㅠㅠㅠ!!!
## 도랏 .. 됐다 정해코드 ..!
d = [(0, 0), (0, 1), (1, 0), (-1, 0), (0, -1)]

def solution(land):
    w, h = len(land[0]), len(land)
    res = [0 for _ in range(w)]
    print(res)
    for i in range(h):
        for j in range(w):
            if land[i][j] == 1:
                queue = [(i, j)]
                minW, maxW, cnt = w, 0, 0
                cnt = 0
                while queue:
                    si, sj = queue.pop(0)
                    for di, dj in d:
                        ni, nj = si+di, sj+dj
                        if 0 <= ni < h and 0 <= nj < w and land[ni][nj] == 1:
                            land[ni][nj] = 2
                            queue.append((ni, nj))
                            cnt += 1
                            minW = min(minW, nj)
                            maxW = max(maxW, nj)
                for l in range(minW, maxW+1):
                    res[l] += cnt

    return max(res)
