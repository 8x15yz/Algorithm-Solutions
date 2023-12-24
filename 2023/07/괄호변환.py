# https://school.programmers.co.kr/learn/courses/30/lessons/60058

def isRight(u):
    stack = []
    for i in u:
        if i == '(': stack.append(i)
        elif i == ')' and not stack: return False
        else: stack.pop()
    else: return True

def solution(p):
    if p == '': return p
    else:
        i, lft, rgt = 0, 0, 0
        while True:
            if lft > 0 and rgt == lft:
                u, v = p[:i], p[i:]
                if isRight(u): 
                    return u+solution(v)
                else:
                    u, retans = u[1:len(u)-1], ''
                    for j in u: 
                        retans = retans+')' if j == '(' else retans+'('
                    return '('+solution(v)+')'+retans
            else:
                if p[i] == ')': rgt += 1
                else: lft += 1
                i += 1
