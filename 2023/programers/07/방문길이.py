#https://school.programmers.co.kr/learn/courses/30/lessons/49994
# 너무 무식하게 풀긴 했어 ..
# 어쩔 컴퓨터가그러러고있는건데 ~ 

route = {"L": (0, -1), "R": (0, 1), "U": (1, 0), "D": (-1, 0)}
def solution(dirs):
    visit = []
    si, sj = 0, 0
    for point in dirs:
        vi, vj = route[point]
        if -5 <= si+vi <= 5 and -5 <= sj+vj <= 5:
            ni = si + vi
            nj = sj + vj
            if (si, sj, ni, nj) not in visit and (ni, nj, si, sj) not in visit: visit.append((si, sj, ni, nj))
            si, sj = ni, nj
    return len(visit)
