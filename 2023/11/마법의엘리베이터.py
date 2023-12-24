#https://school.programmers.co.kr/learn/courses/30/lessons/148653

f = [-1, 1]
def solution(storey):
    answer = 0
    queue = [(storey, 0)]
    while queue:
        n, cnt = queue.pop(0)
        for i in range(0, 9):
            for d in f:
                num = n+d*(10**i)
                if num == 0:
                    answer = min(answer, cnt)
                    break
                if 0 < num <= 10**8:
                    queue.append((num, cnt+1))
    return answer
