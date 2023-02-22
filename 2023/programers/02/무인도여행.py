# bfs dfs 탐색문제
# https://school.programmers.co.kr/learn/courses/30/lessons/154540

def solution(maps):
    answer = []
    d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    # bfs
    for i in range(len(maps)):
        maps[i] = list(maps[i])
    visit = []
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != 'X' and (i,j) not in visit:
                queue = [(i, j)]
                cnt = int(maps[i][j])
                visit.append((i, j))
                while queue:
                    si, sj = queue.pop(0)
                    for di, dj in d:
                        ni, nj = si+di, sj+dj
                        if 0 <= ni < len(maps) and 0 <= nj < len(maps[0]):
                            if maps[ni][nj] != 'X' and (ni, nj) not in visit:
                                cnt += int(maps[ni][nj])
                                queue.append((ni, nj))
                                visit.append((ni, nj))
                else:
                    answer.append(cnt)
                    visit.append((i, j))
    if answer == []:
        answer = [-1]
    else:
        answer = sorted(answer)
    return answer
