# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = 0
    unitDict = {}
    for i in range(1, len(s)//2+1):
        unit = []
        for j in range(0, len(s), i):
            unit.append(s[j:j+i])
        if len(unit[-1]) < len(unit[-2]):
            part = unit.pop()
            unit[-1] += part
        
        ans = ""
        cnt, comp = 1, ""
        for part in unit:
            if comp == part: cnt += 1
            else: 
                if 2 <= cnt: ans += str(cnt)+comp
                else: ans += comp
                cnt, comp = 1, part
        else: 
            if 2 <= cnt: ans += str(cnt)+comp
            else: ans += comp
        unitDict[len(ans)] = ans
    return min(unitDict)
