# 너무쉬웟던문데 ..
## https://school.programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    answer = 0
    s = list(s)
    t = []
    for i in s:
        if i in ['[', ']']: t.append(1)
        elif i in ['(', ')']: t.append(0)
        else: t.append(2)
        
    for i in range(len(s)):
        s.append(s.pop(0))
        t.append(t.pop(0))
        scopy = s.copy()
        stack = []
        for j in range(len(scopy)):
            if scopy[j] in ['(', '{', '[']: stack.append((scopy[j], t[j]))
            elif not stack: break
            elif stack[-1][1] == t[j]: stack.pop()
            else: break
        else: answer += 1 if not stack else answer
            
    return answer
