#https://school.programmers.co.kr/learn/courses/30/lessons/43165

def dfs(numbers, i, tsum, lust, target):
    if i == len(numbers):
        if tsum == target: lust.append(1)
    else:
        dfs(numbers, i+1, tsum-numbers[i], lust, target)
        dfs(numbers, i+1, tsum+numbers[i], lust, target)
        
    return lust
    

def solution(numbers, target):
    return len(dfs(numbers, 0, 0, [], target))
