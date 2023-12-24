#https://school.programmers.co.kr/learn/courses/30/lessons/120866

dt = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (1, -1),(-1, 1)]
def solution(board):
    answer = 0
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for di, dj in dt:
                    if 0 <= i+di < n and 0 <= j+dj < n and board[i+di][j+dj] != 1:
                        board[i+di][j+dj] = 2

    for i in range(n):
        for j in range(n):
            if board[i][j] == 0: answer += 1
    return answer
