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
  
## 두개틀림
def solution(n, lost, reserve):
    answer = 0
    student = [0]
    for i in range(n):
        if i+1 in reserve and i+1 not in lost: # 체육복 하나 남는경우
            student.append(2)
        elif i+1 in reserve and i+1 in lost: # 체육복이 하나밖에 없는 경우 (1)
            student.append(1)
            lost.remove(i+1)
        elif i+1 not in reserve and i+1 not in lost: # 체육복이 하나밖에 없는 경우 (2)
            student.append(1)
        elif i+1 in lost and i+1 not in reserve: # 체육복을 도난당한경우
            student.append(0)
    student.append(0)
    
    for lo in lost:
        if student[lo-1] == 2:
            student[lo-1] = 1
            student[lo] = 1
        elif student[lo+1] == 2:
            student[lo+1] = 1
            student[lo] = 1
    for stu in student:
        if stu != 0:
            answer += 1
            
    return answer


