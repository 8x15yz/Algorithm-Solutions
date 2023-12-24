#https://school.programmers.co.kr/learn/courses/30/lessons/42839


from itertools import permutations
def solution(numbers):
    answer = 0
    numlen = len(numbers)
    prime = set()
    for i in range(1, numlen+1):
        permu = permutations(list(numbers), i)
        for x in list(set(permu)):
            x = int(''.join(list(x)))
            for j in range(x-1, 1, -1):
                if x%j == 0: break
            else:
                if x != 1 and x != 0: prime.add(x)

    return len(prime)


# 맞은코드
from itertools import permutations
from math import sqrt

def solution(numbers):
    numlen = len(numbers)
    prime = set()
    for i in range(1, numlen+1):
        permu = permutations(list(numbers), i)
        for x in list(set(permu)):
            x = int(''.join(list(x)))
            if x == 1 or x == 0: continue
            for j in range(2, int(sqrt(x))+1):
                if x%j == 0: break
            else:
                prime.add(x)

    return len(prime)
