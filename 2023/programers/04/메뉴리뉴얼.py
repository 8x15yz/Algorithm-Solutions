#https://school.programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations

def isDuplicate(dishes, compareTuple):
    for dish in dishes:
        for d in compareTuple:
            if d not in dish: break
        else: return 'already'
    else: return ''.join(compareTuple)

def solution(orders, course):
    answer = []
    dishD = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
             'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
             'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
    
    orderList = [[0]*26 for _ in range(len(orders))]
    
    for o in range(len(orders)):
        for order in orders[o]:
            orderList[o][dishD[order]] = 1
    course = sorted(course, reverse=True)
    for i in course:
        for alpha in list(combinations(dishD, i)):
            cnt = 0
            for j in range(len(orderList)):
                combi = 1
                for di in alpha:
                    combi *= orderList[j][dishD[di]]
                    if combi == 0: break
                else:
                    cnt += 1
                    if cnt > 1:
                        isDup = isDuplicate(answer, alpha)
                        if isDup != 'already': answer.append(isDup)
                        break
    
    return answer
