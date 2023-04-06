#https://school.programmers.co.kr/learn/courses/30/lessons/64065
# 이 코드 너무 무식하다는 생각이 들긴 했어 ..
def solution(s):
    ans = []
    answer = []
    cnt = []
    s = s[1:-1]
    strtoint = ''
    ct = 1
    
    for i in range(len(s)):
        if s[i] == '{':
            answer.append([])
        elif s[i] == '}':
            cnt.append(ct)
            ct = 0
            if i < len(s)-1 and s[i+1] == ',': continue
            elif i == len(s)-1:
                answer[-1].append(int(strtoint))
                ct += 1
        elif s[i] == ',': 
            answer[-1].append(int(strtoint))
            ct += 1
            strtoint = ''
        else:
            strtoint += s[i]
            
    for i in range(1, max(cnt)+1):
        for j in answer[cnt.index(i)]:
            if j not in ans:
                ans.append(j)
                break

    return ans
