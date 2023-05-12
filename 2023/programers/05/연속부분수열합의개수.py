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
