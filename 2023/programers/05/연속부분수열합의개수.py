# 풀고있는중 ..
# https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
    answer = 0
    sumSet = set()
    for i in range(2, len(elements)+1):
        sp = 0
        ep = sp+i
        cnt = 0
        while cnt < len(elements):
            sp = (sp+1)%len(elements)
            ep = (ep+1)%len(elements)
            cnt += 1
            print(sp, ep, elements[sp:ep])
            
        break
    
    return answer


## 풀이완
def solution(elements):
    sumSet = set()
    for i in range(1, len(elements)+1):
        sp = 0
        ep = sp+i
        cnt = 0
        while cnt < len(elements):
            if ep <= sp: sumSet.add(sum(elements[sp:])+sum(elements[:ep]))
            else: sumSet.add(sum(elements[sp:ep]))
            sp = (sp+1)%len(elements)
            ep = (ep+1)%len(elements)
            cnt += 1
    
    return len(sumSet)
