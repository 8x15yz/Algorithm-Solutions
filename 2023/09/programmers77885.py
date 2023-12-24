## https://school.programmers.co.kr/learn/courses/30/lessons/77885
## 이거 너무 사긴데 ..

def solution(numbers):
    answer = []
    for num in numbers:
        ans = ((num ^ (num+1)) >> 2) + num + 1
        answer.append(ans)
    return answer
