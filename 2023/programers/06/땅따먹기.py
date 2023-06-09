# https://school.programmers.co.kr/learn/courses/30/lessons/12913
def solution(land):
    answer = 0
    # 같은 열 연속 불rk
    L = len(land)
    for c in range(4):
        dp = [0 for _ in range(L)]
        checkL = c
        dp[0] = land[0][c]
        for i in range(1, L):
            maxL = -1
            for j in range(4):
                if maxL < land[i][j] and j != checkL: 
                    maxL = land[i][j]
                    fCheck = j
            else: 
                checkL = fCheck
                dp[i] = dp[i-1] + maxL
        else:
            answer = dp[-1] if answer < dp[-1] else answer
    
    return answer


# 계속 푸는중
def solution(land):
    answer = [0 for _ in range(len(land))]
    path = [-1 for _ in range(len(land))]
    basket = []
    duplicateFlag = -2
    for i in range(len(land)):
        comp = -1
        duplicateCheck = [0, 0, 0, 0]
        for j in range(4):
            if land[i].count(land[i][j]) > 1 and land[i][j] >= comp:
                duplicateFlag = i-1 if duplicateFlag == -2 else duplicateFlag
                if land[i][j] > comp: duplicateCheck = [0, 0, 0, 0]
                duplicateCheck[j], comp = 1, land[i][j]
                    
            elif land[i][j] > comp and i == 0 or land[i][j] > comp and j != path[i-1]:
                path[i], comp = j, land[i][j]
                duplicateCheck = [0, 0, 0, 0]
                
        else:
            if sum(duplicateCheck) == 0: 
                answer[i] = comp
                if basket:
                    basket[0][path[duplicateFlag]] = 0
                    basket[-1][path[i]] = 0
                    cRange = i-duplicateFlag-1
                    for k in range(cRange):
                        for l in range(4):
                            if basket[k][l] == 1:
                                path[k+duplicateFlag+1] = l
                                answer[k+duplicateFlag+1] = land[duplicateFlag+1+k][l]
                                if k < cRange-1: basket[k+1][l] = 0
                                break
                    else:
                        duplicateFlag = -2
                        basket = []
            else: basket.append(duplicateCheck)
    return sum(answer)


## 0609 빵점코드 ㅠㅠ
def solution(land):
    #land = [[4, 3, 2, 1], [2, 2, 3, 3], [1, 1, 1, 1], [3, 4, 5, 6], [1, 1, 1, 1], [6, 6, 6, 3], [7, 8, 6, 5]]
    # land = [[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]
    
    #land = [[1, 1, 1, 4], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 3, 1]]
    answer = [0 for _ in range(len(land))]
    path = [-1 for _ in range(len(land))]
    basket = []
    duplicateFlag = -2
    for i in range(len(land)):
        comp = -1
        duplicateCheck = [0, 0, 0, 0]
        for j in range(4):
            if land[i].count(land[i][j]) > 1 and land[i][j] >= comp:
                duplicateFlag = i-1 if duplicateFlag == -2 else duplicateFlag
                if land[i][j] > comp: duplicateCheck = [0, 0, 0, 0]
                duplicateCheck[j], comp = 1, land[i][j]
                    
            elif land[i][j] > comp and i == 0 or land[i][j] > comp and j != path[i-1]:
                path[i], comp = j, land[i][j]
                duplicateCheck = [0, 0, 0, 0]
                
        else:
            if sum(duplicateCheck) == 0: 
                answer[i] = comp
                if basket:
                    basket[0][path[duplicateFlag]] = 0
                    basket[-1][path[i]] = 0
                    duplicateFlag = 0 if duplicateFlag == -1 else duplicateFlag
                    cRange = i-duplicateFlag-1 
                    for k in range(cRange):
                        for l in range(4):
                            if basket[k][l] == 1:
                                path[k+duplicateFlag+1] = l
                                answer[k+duplicateFlag+1] = land[duplicateFlag+1+k][l]
                                if k < cRange-1: basket[k+1][l] = 0  
                                break
                    else:
                        duplicateFlag = -2
                        basket = []
            else: basket.append(duplicateCheck)
    return sum(answer)
