#https://school.programmers.co.kr/learn/courses/30/lessons/120871

no3 = [0, 1, 2]
for i in range(3, 200):
    if i%3 == 0 or "3" in str(i): continue
    no3.append(i)
    
def solution(n):
    return no3[n]
