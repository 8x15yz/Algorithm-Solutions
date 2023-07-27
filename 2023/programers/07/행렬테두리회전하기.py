# https://school.programmers.co.kr/learn/courses/30/lessons/77485

# 푸는중
def solution(rows, cols, queries):
    arr = [[i*cols+j+1 for j in range(cols)] for i in range(rows)]
    answer = []
    for que in queries:
        si, sj = que[0]-1, que[1]-1
        ei, ej = que[2]-1, que[3]-1
        min = 999999999
        for route, plus, target in [(ej-sj, 1, "j"), (ei-si, 1, "i"), (ej-sj, -1, "j"), (ei-si, -1, "i")]:     
            for _ in range(route):
                if min > arr[si][sj]: min = arr[si][sj]
                if target == "i": 
                    si += plus
                    arr[si-1][sj], arr[si][sj] = arr[si][sj], arr[si-1][sj]
                elif target == "j": 
                    sj += plus
                    arr[si][sj-1], arr[si][sj] = arr[si][sj], arr[si][sj-1]
        else: 
            answer.append(min)
    
    return answer
