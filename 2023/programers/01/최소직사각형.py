# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    answer = 0
    width = 0
    height = 0
    for size in sizes:
        size = sorted(size)
        if width < size[0]:
            width = size[0]
        if height < size[1]:
            height = size[1]
    answer = height * width
    return answer
