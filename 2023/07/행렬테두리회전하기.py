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
def solution(rows, cols, queries):
    answer = []
    note1, note2, note3, note4= 0, 0, 0, 0
    arr = [['{0:02d}'.format(i*cols+j+1) for j in range(cols)] for i in range(rows)]
    for que in queries:
        min = 99999
        note4 = arr[que[0]-1][que[1]-1]
        for j in range(que[3]-1, que[1]-1, -1):
            min = int(arr[que[0]-1][j]) if int(arr[que[0]-1][j]) < min else min
            if j == que[1]: arr[que[0]-1][j] = note4
            else:
                if j == que[3]-1 : note1 = arr[que[0]-1][j]
                arr[que[0]-1][j] = arr[que[0]-1][j-1]
            
        for j in range(que[2]-1, que[0]-1, -1):
            min = int(arr[j][que[3]-1]) if int(arr[j][que[3]-1]) < min else min
            if j == que[0]: arr[j][que[3]-1] = note1
            else:
                if j == que[2]-1 : note2 = arr[j][que[3]-1]
                arr[j][que[3]-1] = arr[j-1][que[3]-1]

        for j in range(que[1]-1, que[3]-1):
            min = int(arr[que[2]-1][j]) if int(arr[que[2]-1][j]) < min else min
            if j == que[3]-2: arr[que[2]-1][j] = note2
            else:
                if j == que[1]-1 : note3 = arr[que[2]-1][j]
                arr[que[2]-1][j] = arr[que[2]-1][j+1]

        for j in range(que[0]-1, que[2]-1):
            min = int(arr[j][que[1]-1]) if int(arr[j][que[1]-1]) < min else min
            if j == que[2]-2: arr[j][que[1]-1] = note3
            else:
                arr[j][que[1]-1] = arr[j+1][que[1]-1]

        answer.append(min)
        
        
            
    return answer
# 난 이것도 글러먹었다고 생각해 


# 0728 다시시도중
def ViewArr(arr):
    for a in arr:
        print(a)
    print()
def solution(rows, cols, queries):
    # rows, cols, queries = 3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
    answer = []
    arr = [['{0:02d}'.format(i*cols+j+1) for j in range(cols)] for i in range(rows)]
    ViewArr(arr)
    
    for  que in queries:
        si, sj, ei, ej = que[0]-1, que[1]-1, que[2]-1, que[3]-1
        note4 = arr[si][sj]
        for j in range(ej, sj, -1):
            if j == sj-1: arr[si][j] = note4
            else:
                if j == ej: note1 = arr[si][j]
                arr[si][j] = arr[si][j-1]
            # print(arr[si][j], arr[si][j-1])
        # si = -1 if si == 0 else si
        si = si-1 if ei-si <= 1 else si
        for i in range(ei, si, -1):
            if i == si+1: arr[i][ej] = note1
            else: 
                if i == ei: note2 = arr[i][ej]
                arr[i][ej] = arr[i-1][ej]
        # ej = 2 if ej == 1 else ej
        ej = ej + 1 if ej-sj <= 1 else ej
        for j in range(sj, ej):
            if j == ej-1: arr[ei][j] = note2
            else:
                if j == sj: note3 = arr[ei][j]
                arr[ei][j] = arr[ei][j+1]
        for i in range(si, ei):
            if i == ei-1: arr[i][sj] = note3
            else: arr[i][sj] = arr[i+1][sj]
        ViewArr(arr)
            
            
    return answer
