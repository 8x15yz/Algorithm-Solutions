# https://school.programmers.co.kr/learn/courses/30/lessons/12969
# 문제도 아님
a, b = map(int, input().strip().split(' '))
for i in range(b):
    for j in range(a):
        print('*', end='')
    print()
