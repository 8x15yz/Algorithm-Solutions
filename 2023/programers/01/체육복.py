# https://school.programmers.co.kr/learn/courses/30/lessons/42862
# 틀린코드
def solution(n, lost, reserve):
    answer = 0
    student = [0 for _ in range(n)]
    
    for res in reserve:
        if res in lost:
            continue
        else:
            student[res-1] = 1
    for lo in lost:
        if lo in reserve:
            continue
        else:
            student[lo-1] = 2
    
    for i in range(1, n-1):
        if student[i] == 1:
            if student[i-1] == 2:
                student[i] = 0
                student[i-1] = 0
    else:
        if student[len(student)-2] == 1 and student[-1] == 2:
            student[len(student)-2] = 0
            student[-1] = 0
        elif student[-1] == 1 and student[len(student)-2] == 2:
            student[len(student)-2] = 0
            student[-1] = 0
            
    for st in student:
        if st == 0 or st == 1:
            answer += 1
        
    return answer
  
## 맞은코드
