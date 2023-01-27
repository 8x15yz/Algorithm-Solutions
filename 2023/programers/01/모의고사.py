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



# 정답코드 이거 근데 틀린코드 왜 런타임에러 나는지 모르겠다
def solution(answers):
    answer = []
    
    student = ['12345','21232425','3311224455']
    stscore =  [0, 0, 0]
    
    for i, ans in enumerate(answers):
        if int(student[0][i%5]) == ans:
            stscore[0]+= 1
        if int(student[1][i%8]) == ans:
            stscore[1]+= 1
        if int(student[2][i%10]) == ans:
            stscore[2]+= 1
    
    for i in range(3):
        if stscore[i] == max(stscore):
            answer.append(i+1)
            
    return answer
