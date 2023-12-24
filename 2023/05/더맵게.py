#https://school.programmers.co.kr/learn/courses/30/lessons/42626?language=python3

# 난장판코드
def solution(scoville, K):
    answer = 0
    while True:
        scoville.sort()
        if len(scoville) < 2: return -1
        elif scoville[0] < K: 
            scoville = [scoville[0]*scoville[1]*2] + scoville[2:]
            answer += 1
        else: return answer


# 정확성만점인데 효율성거지
def solution(scoville, K):
    answer = 0
    while len(scoville) > 1:
        scoville.sort()
        if scoville[0] >= K: return answer
        scoville = [scoville[0]+scoville[1]*2] + scoville[2:]
        answer += 1
        
    if scoville[0] < K: return -1
    else: return answer
   


# 힙으로 만들고 있는중
def heap(sco):
    vNode = 1
    while vNode**2 < len(sco):
        if sco[vNode*2] < sco[vNode*2+1] and sco[vNode*2] < sco[vNode]: 
            sco[vNode], sco[vNode*2] = sco[vNode*2], sco[vNode]
            vNode = vNode*2
        elif sco[vNode*2+1] < sco[vNode*2] and sco[vNode*2+1] < sco[vNode]: 
            sco[vNode], sco[vNode*2+1] = sco[vNode*2+1], sco[vNode]
            vNode = vNode*2+1
    return sco

def solution(sco, K):
    answer = 0
    sco += [0]
    sco.sort()
    sSco = [0, 0]
    if sco[1] < K: 
        for i in range(2):
            sSco[i], sco[1] = sco[1], sco.pop() # 삭제해서 루트로 올림
            heap(sco)
            
    sumSco = sSco[0]+sSco[1]*2
    sco.append(sumSco)
    print(sumSco, sco)
    
    
    
    
