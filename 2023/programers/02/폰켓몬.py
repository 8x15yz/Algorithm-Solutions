# https://school.programmers.co.kr/learn/courses/30/lessons/1845
# 조합으로 했더니 시간초과 ..
from itertools import combinations
def solution(nums):
    answer = 0
    N = len(nums)
    N2 = int(len(nums)/2)
    ans = []
    for pset in list(combinations(nums, N2)):
        ans.append(len(set(list(pset))))
    answer = max(ans)
    return answer
  
# 이것도 시간초과 ..
from itertools import combinations
def solution(nums):
    answer = 0
    n = len(nums)//2
    for pset in list(combinations(nums, n)):
        if len(set(list(pset))) == n:
            answer = n
            break
        else:
            if answer < len(set(list(pset))):
                answer = len(set(list(pset)))
    return answer
