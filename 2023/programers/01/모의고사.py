# https://school.programmers.co.kr/learn/courses/30/lessons/42840
# 런타임에러 왜뜨는거임

def solution(answers):
    answer = []
    # 12345
    # 2123242
    # 331122445
    student = ['12345','21232425','331122445']
    stscore =  [0, 0, 0]
    stid = [0, 0, 0]
    for i in range(3):
        for ans in answers:
            if int(student[i][stid[i]]) == ans:
                stscore[i] += 1
            stid[i] += 1
            if stid[i]+1 == len(student[i]):
                stid[i] == 0
    
    for i in range(3):
        if stscore[i] == max(stscore):
            answer.append(i+1)
            
    return answer
