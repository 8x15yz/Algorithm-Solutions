# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    for h in range(max(citations), 0, -1):
        # h번 이상 인용된 논문이 있으면 count
        # count >= h : True
        # len(citations) - count <= h : True
        cnt = 0
        for cite in citations:
            if cite >= h:
                cnt += 1
        else:
            if cnt >= h and len(citations) - cnt <= h:
                answer = h
                break
    return answer
