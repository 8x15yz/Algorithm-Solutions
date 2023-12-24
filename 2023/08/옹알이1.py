#https://school.programmers.co.kr/learn/courses/30/lessons/120956
# 이렇게 쉬왓던 것을 약 1년간 못풀고 있었다는거야 ..

def solution(babbling):
    answer = 0 
    for babb in babbling:
        sentence = ""
        for b in babb:
            sentence += b
            if sentence in ["aya", "ye", "woo", "ma"]:
                sentence = ""
        if sentence == "": answer += 1
    return answer
