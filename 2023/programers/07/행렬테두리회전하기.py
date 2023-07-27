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
# 이건 글러먹은 코드다 처음부터 다시 쓰기

def viewArr(arr):
    for a in arr:
        print(a)
        
def solution(rows, cols, queries):
    answer = []
    arr = [[i*cols+j+1 for j in range(cols)] for i in range(rows)]
    for que in queries:
        note1, note2, note3, note4 = 0, 0, 0, 0
        for j in range(que[3]-1, que[1]-1, -1):
            print(arr[que[0]-1][j], arr[que[0]-1][j-1])
        # viewArr(arr)
        print()
        for j in range(que[2]-1, que[0]-1, -1):
            print(arr[j][que[3]-1], arr[j-1][que[3]-1])
        # viewArr(arr)
        print()
        for j in range(que[1]-1, que[3]-1):
            print(arr[que[2]-1][j], arr[que[2]-1][j+1])
        # viewArr(arr)
        print()
        for j in range(que[0]-1, que[2]-1):
            print(arr[j][que[1]-1], arr[j+1][que[1]-1])
        # viewArr(arr)
        print()
        
        
        
            
    return answer
