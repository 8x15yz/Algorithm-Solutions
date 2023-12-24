# https://school.programmers.co.kr/learn/courses/30/lessons/12947
# pythonic 하게 짜보려 했으나 .. 52.9점
def solution(x):
    answer = bool(sum(list(map(int, list(str(x)))))//x)
    return answer
  
# 정답코드
# 문제를 잘읽고 메서드에 신경쓰기 ~
def solution(x):
    return not bool(x%sum(list(map(int, list(str(x))))))
  
