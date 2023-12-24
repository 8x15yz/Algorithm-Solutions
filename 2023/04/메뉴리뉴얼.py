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


# 이숑키봐라 ...
def solution(orders, course):
    answer = []
    foodDict = {}
    for d in range(len(orders)):
        for dish in orders[d]:
            if dish not in foodDict: foodDict[dish] = {d+1}
            else: foodDict[dish].add(d+1)
    
    multiply = []
    for dish in foodDict:
        for comp in foodDict:
            if dish == comp: continue
            else:
                mul = tuple(foodDict[dish] & foodDict[comp])
                if len(mul) > 1 and mul not in multiply: multiply.append(mul)
    
    for mul in multiply:
        ans = []
        for dish in foodDict:
            for m in mul:
                if m not in foodDict[dish]: break
            else: ans += [dish]
        else:
            if ans != '': answer.append(''.join(sorted(ans)))
                    
    return sorted(answer)


# 풀었다 ~~~ ㅠㅠㅠㅠ
from itertools import combinations
def solution(orders, course):
    answer = []
    courseDict = [{} for _ in range(len(course))]
    for order in orders:
        for i in range(len(course)):
            for a in list(combinations(order, course[i])):
                ord = ''.join(sorted(a))
                if ord in courseDict[i]: courseDict[i][ord] += 1
                else: courseDict[i][ord] = 1
    
    for course in courseDict:
        maxNum = 2
        maxCourse = []
        for cour in course:
            if course[cour] > maxNum:
                maxNum = course[cour]
                maxCourse = [cour]
            elif course[cour] == maxNum:
                maxCourse.append(cour)
        else: answer += maxCourse
        
    return sorted(answer)
