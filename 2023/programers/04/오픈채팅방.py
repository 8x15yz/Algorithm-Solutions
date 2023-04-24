#https://school.programmers.co.kr/learn/courses/30/lessons/42888

# 너무 쉬운 문제엿어
def solution(record):
    answer = []
    IOdict, UserAct = {}, []
    inOut = ['님이 들어왔습니다.', '님이 나갔습니다.']
    actDict = {'Enter' : 0, 'Leave':1}
    
    for rec in record:
        UserStatus = list(rec.split())
        UserAct.append((UserStatus[1], UserStatus[0]))
        if UserStatus[0] != 'Leave':
            if UserStatus[1] not in IOdict:
                IOdict[UserStatus[1]] = UserStatus[2]
            else: IOdict[UserStatus[1]] = UserStatus[2]
    
    for act in UserAct:
        if act[1] != 'Change': answer.append(IOdict[act[0]]+inOut[actDict[act[1]]])
        
    return answer
