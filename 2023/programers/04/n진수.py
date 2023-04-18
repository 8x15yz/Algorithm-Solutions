# https://school.programmers.co.kr/learn/courses/30/lessons/17687

def changeOrder(order, n, nth):
    if order[nth] == n:
        if len(order) == nth+1:
            order.append(1)
        else:
            order[nth+1] += 1
        order[nth] = 0
    return order, len(order)

def solution(n, t, m, p):
    answer = ''
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    cnt, digitOrder, out, flag = 0, [0], 0, True 
    
    while flag:
        for j in range(len(digitOrder)):
            digitOrder, lenOrder = changeOrder(digitOrder,n, j)
        
        for i in range(lenOrder):
            if out%m+1 == p:
                answer += numbers[list(reversed(digitOrder))[i]]
                cnt += 1
                if cnt == t: 
                    flag = False
                    break
            out += 1
        digitOrder[0] += 1
        
    return answer
