# https://school.programmers.co.kr/learn/courses/30/lessons/12948
def solution(phone_number):
    phone_number = list(phone_number)
    answer = ''
    for i in range(len(phone_number)-4):
        phone_number[i] = '*'
    answer = ''.join(phone_number)
    return answer
