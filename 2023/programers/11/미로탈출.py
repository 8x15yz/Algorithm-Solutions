# https://school.programmers.co.kr/learn/courses/30/lessons/159993
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
def solution(maps):
    answer = -1
    h, w = len(maps), len(maps[0])
    def findL():
        for i in range(h):
            for j in range(w):
                if maps[i][j] == "S":
                    visit = []
                    queue = [(i, j)]
                    while queue:
                        si, sj = queue.pop(0)
                        if maps[si][sj] == "L": return si, sj
                        for di, dj in d:
                            ni, nj = di+si, dj+sj
                            if 0 <= ni < h and 0 <= nj < w and maps[ni][nj] != "X" and (ni, nj) not in visit:
                                queue.append((ni, nj))
                                visit.append((ni, nj))
        return -1
    mid = findL()
    
    if mid == -1: return -1
    else:
        def findE():
            visit = []
            queue = [mid]
            while queue:
                si, sj = queue.pop(0)
                if maps[si][sj] == "E": return si, sj
                for di, dj in d:
                    ni, nj = di+si, dj+sj
                    if 0 <= ni < h and 0 <= nj < w and maps[ni][nj] != "X" and (ni, nj) not in visit:
                        queue.append((ni, nj))
                        visit.append((ni, nj))
        return -1
        print(findE())
        
    return answer
