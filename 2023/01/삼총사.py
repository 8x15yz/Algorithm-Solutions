# 

# 틀린 답 => 이터툴즈 안쓰고 깡코딛으로 조합 만들려고 했는데 안된 코드
# 나중에 또 보면서 코드 고쳐볼 수 있으면 조켓다
def comb(p, n, i):
    if i == r:
        if sum(p) == 0:
            answer += 1
        return 
    if len(p) == 0:
        smallest = 0
    else:
        smallest = p[-1]
    for k in range(smallest, n):
        if number[k] not in p:
            p.append(number[k])
            comb(p, n, i+1)
            p.pop()
def solution(number):
    answer = 0
    r = 3
    comb([], len(number),0)
    return answer
  

# 정답코드
from itertools import combinations
def solution(number):
    answer = 0
    for a in list(combinations(number, 3)):
        if sum(a) == 0:
            answer += 1
    return answer
