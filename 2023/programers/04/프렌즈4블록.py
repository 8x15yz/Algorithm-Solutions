# https://school.programmers.co.kr/learn/courses/30/lessons/17679

deltas = [[(-1, 0), (-1, 1), (0, 1)], [(0, 1), (1, 1), (1, 0)], [(1, 0), (1, -1), (0, -1)], [(0, -1), (-1, -1), (-1, 0)]]
def solution(M, N, board):
    answer = 0
    # 1 턴 구현
    board = list(map(list, board))
    check = [[0]*N]*M
    for a in board:
        print(a)
    print()
    for m in range(M):
        for n in range(N):
            for delta in deltas:
                checkBox = []
                for dm, dn in delta:
                    if 0 <= dm+m < M and 0 <= dn+n <N and board[dm+m][dn+n] == board[m][n]:
                        # print(dm+m, dn+n, board[dm+m][dn+n])
                        checkBox.append((dm+m, dn+n))
                    else: break
                else:
                    print(m, n, checkBox)
                    for i, j in checkBox:
                        check[i][j] = 1
    
    for a in check:
        print(a)
                        
    return answer
