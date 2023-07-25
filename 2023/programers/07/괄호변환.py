# https://school.programmers.co.kr/learn/courses/30/lessons/60058
#푸는중

def isRight(u):
    stack = []
    for i in u:
        if i == '(': stack.append(i)
        elif i == ')' and !stack: return False
        else: stack.pop()
    else: return True

def solution(p):
    if p == '': return p
    else:
        i, lft, rgt = 0, 0, 0
        while True:
            if lft > 0 and rgt == lft:
                u, v = p[:i], p[i:]
                if isRight(u): return u+solution(v)
                else:
                    u = u[1:len(u)-1]
                    retans = '('
                    for j in u:
                        if j == '(': retans += ')'
                        else: retans += '('
                    return retans+solution(v)
            if p[i] == ')': rgt += 1
            else: lft += 1
            i += 1
