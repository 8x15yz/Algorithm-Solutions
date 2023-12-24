#https://school.programmers.co.kr/learn/courses/30/lessons/17677

# 다중교집합, 다중합집합 코드 공부 햇다 
# https://prod.velog.io/@tlsdnxkr/Python-%EB%8B%A4%EC%A4%91%ED%95%A9%EC%A7%91%ED%95%A9-%EB%8B%A4%EC%A4%91%EA%B5%90%EC%A7%91%ED%95%A9


def solution(str1, str2):
    set1, set2 = [], []
    str1, str2 = str1.lower(), str2.lower()
    
    for i in range(max(len(str1), len(str2))):
        part1 = str1[i:i+2]
        part2 = str2[i:i+2]
        if len(part1) == 2 and part1.isalpha(): set1.append(part1)
        if len(part2) == 2 and part2.isalpha(): set2.append(part2)
            
    uni, set1copy= set1.copy(), set1.copy()
    for word in set2:
        if word not in set1copy: 
            uni.append(word)
        else: set1copy.remove(word)

    inter = []
    for word in set2:
        if word in set1:
            inter.append(word)
            set1.remove(word)

    if len(inter)*len(uni) == 0:
        answer = 65536 if len(inter) == 0 and len(uni) == 0 else 0
    else:
        answer = int(65536*(len(inter)/len(uni)))

    return answer
