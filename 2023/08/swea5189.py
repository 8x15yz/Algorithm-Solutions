# swea 5189 (Programming Advanced : 2일차 - 전자카트)
import sys
sys.stdin = open('sample_input.txt', 'r')

import itertools 

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    minval = 99999
    for case in list(itertools.permutations(range(1, n), n-1)):
        case = [0]+list(case)+[0]
        route = 0
        for c in range(1, len(case)):
            route += arr[case[c-1]][case[c]]
        else: 
            if route < minval: minval = route
    print('#{} {}'.format(tc, minval))
