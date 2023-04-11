# https://school.programmers.co.kr/learn/courses/30/lessons/92335

## 테케 12번 런타임에러 왜그럴까 ???
def isPrime(number):
    if number == 1: return 0
    for k in range(2, int(number**(0.5))+1):
        if number%k == 0: return 0
    else: return 1

def solution(n, k):
    expo, flag = 0, True
    while flag:
        for i in range(k-1, 0, -1):
            if i*(k**expo) >= n: 
                flag = False
                break
        else: expo += 1
    
    order = [0]*(expo+1)
    for i in range(expo, -1, -1):
        for j in range(k-1, -1, -1):
            if n >= (k**i)*j:
                n -= (k**i)*j
                order[expo-i] = j
                break
    
    number = ''
    i = 0
    
    answer = 0
    while i < len(order):
        if order[i] == 0 and number != '':
            answer += isPrime(int(number))
            number = ''
        elif order[i] != 0: number += str(order[i])
        i += 1
    else: answer += isPrime(int(number))
            
    return answer
