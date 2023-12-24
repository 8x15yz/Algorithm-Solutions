#https://school.programmers.co.kr/learn/courses/30/lessons/92341

from math import ceil
def solution(fees, records):
    answer = []
    InRecord, IORec, cars = {}, {}, []
    
    for record in records:
        H, M, code, IO = int(record[:2]), int(record[3:5]), int(record[6:10]), record[11:]
        if code not in cars: cars.append(code)
        if record[11:] == "IN": 
            if code in InRecord: InRecord[code].append(H*60+M)
            else: InRecord[code] = [H*60+M]
            IORec[code] = 'IN'
        elif record[11:] == "OUT": 
            InRecord[code][-1] = H*60+M-InRecord[code][-1]
            IORec[code] = 'OUT'
    
    for a in list(sorted(cars)):
        if IORec[a] == 'IN': InRecord[a][-1] = 23*60+59-InRecord[a][-1]
        if fees[0] < sum(InRecord[a]):
            answer.append(fees[1]+ceil((sum(InRecord[a])-fees[0])/fees[2])*fees[3])
        else: answer.append(fees[1])
            
    return answer
