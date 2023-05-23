# https://school.programmers.co.kr/learn/courses/30/lessons/42577

# 시간초과 ..
def solution(phone_book):
    answer = True
    
    for num in phone_book:
        for ber in phone_book:
            if ber == num: continue
            elif ber[:len(num)] == num: return False
    return answer
