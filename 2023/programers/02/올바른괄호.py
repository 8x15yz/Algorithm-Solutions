#https://school.programmers.co.kr/learn/courses/30/lessons/12909

# 틀린코드
def solution(s):
    s = list(s)
    answer = True
    stack = [s.pop(0)]
    while s:
        n = s.pop(0)
        if n == ')':
            stack.pop()
        else:
            stack.append(n)
    if stack == []:
        answer = True
    else:
        answer = False
    return answer
  
# 맞은코드
