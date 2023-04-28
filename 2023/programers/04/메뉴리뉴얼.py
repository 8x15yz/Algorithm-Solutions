#https://school.programmers.co.kr/learn/courses/30/lessons/72411

def solution(orders, course):
    answer = []
    foodDict = {}
    for d in range(len(orders)):
        for dish in orders[d]:
            if dish not in foodDict: foodDict[dish] = [d+1]
            else: foodDict[dish].append(d+1)
    
    # 교집합이 course개인  문자들의 조합을 모두 출력
    # 인 것 같은데?
    
    
    print(foodDict)
    return answer
