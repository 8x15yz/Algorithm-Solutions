# https://school.programmers.co.kr/learn/courses/30/lessons/17679

deltas = [[(-1, 0), (-1, 1), (0, 1)], [(0, 1), (1, 1), (1, 0)], [(1, 0), (1, -1), (0, -1)], [(0, -1), (-1, -1), (-1, 0)]]
def matchingBlock(board, N, M, answer):
    checkBox = []
    for m in range(M):
        for n in range(N):
            for delta in deltas:
                checkBoxInner = []
                for dm, dn in delta:
                    if 0 <= dm+m < M and 0 <= dn+n <N and board[dm+m][dn+n] == board[m][n]:
                        checkBoxInner.append((m, n))
                        checkBoxInner.append((dm+m, dn+n))
                    else: break
                else:
                    checkBox += checkBoxInner
    else:
        for i, j in checkBox:
            if board[i][j] != '0':
                board[i][j] = '0'
                answer += 1
    return (board, answer)

def relocatingBlock(board, N, M):
    for n in range(N):
        for _ in range(M):
            for m in range(1, M):
                if board[m][n] == '0':
                    board[m][n], board[m-1][n] = board[m-1][n], board[m][n]
    return board

def solution(M, N, board):
    answer = 0
    board = list(map(list, board))
    
    while True:
        matchResult, answer = matchingBlock(board, N, M, answer)
        relocateResult = relocatingBlock(matchResult.copy(), N, M)
        if matchResult == relocateResult: break
        else: board = relocateResult     
    return answer
























