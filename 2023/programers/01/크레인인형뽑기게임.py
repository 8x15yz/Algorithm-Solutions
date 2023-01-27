# https://school.programmers.co.kr/learn/courses/30/lessons/64061
# 구현문제 재밌다

def solution(board, moves):
    answer = 0
    bucket = []
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] != 0:
                if len(bucket) > 0 and bucket[-1] == board[i][m-1]:
                    bucket.pop()
                    answer += 2
                else:
                    bucket.append(board[i][m-1])
                board[i][m-1] = 0
                break
                
    return answer
