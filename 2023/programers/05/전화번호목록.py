# https://school.programmers.co.kr/learn/courses/30/lessons/42577

# 시간초과 ..
def solution(phone_book):
    answer = True
    
    for num in phone_book:
        for ber in phone_book:
            if ber == num: continue
            elif ber[:len(num)] == num: return False
    return answer


# 신기하다 딕셔너리로 푸니까 효율성 통과함
def solution(phone_book):
    answer = True
    phoneDict = {}
    
    for num in phone_book:
        phoneDict[num] = ''
    
    for num in phone_book:
        for i in range(1, len(num)):
            if num[:i] in phoneDict: return False
    return answer
