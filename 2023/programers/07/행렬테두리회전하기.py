# https://school.programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, cols, queries):
    arr = [[i*cols+j+1 for j in range(cols)] for i in range(rows)]
    answer = []
    for que in queries:
        si, sj = que[0]-1, que[1]-1
        ei, sj = que[2]-1, que[3]-1
        
        
    return answer
