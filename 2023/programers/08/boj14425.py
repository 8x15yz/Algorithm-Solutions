# https://www.acmicpc.net/problem/14425

# import sys
# sys.stdin = open('test.txt', 'r')
N, M = map(int, input().split())
S = {}
for _ in range(N):
    pointer = S
    for word in input():
        if word not in pointer:
            pointer[word] = {}
        pointer = pointer[word]
cnt = 0
for _ in range(M):
    pointer = S
    this = input()
    for word in this:
        if word not in pointer: break
        pointer = pointer[word]
    else: 
        if pointer == {}: cnt += 1

print(cnt)

# 틀렷네 이게 왜틀림
