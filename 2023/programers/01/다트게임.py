# https://school.programmers.co.kr/learn/courses/30/lessons/17682
# 틀린코드 ㅠㅠ 
def solution(dartResult):
    answer = 0
    round , bonus, option = [0, 0, 0], ['', '', ''], ['', '', '']
    i, digit = -1, ''
    bonuscnt = {'S' : 1, 'D' : 2, 'T' : 3}
    # isalpha isdigit isalnum 사용
    # 알파벳 바로 앞에는 항상 숫자
    for dt in dartResult:
        if dt.isdigit():
            digit += dt
        elif dt.isalpha():
            i += 1
            round[i] = int(digit)
            digit = ''
            bonus[i] = dt
        elif dt.isalnum() == False:
            option[i] = dt
    
    op = 0
    for i in range(3):
        # 보너스 계산
        round[i] = round[i]**bonuscnt[bonus[i]]
        
        # 옵션 계산
        if option[i] == '*':
            if i != 0:
                round[i-1] *= 2
            round[i] *= 2
        elif option[i] == '#':
            if i != 0:
                if option[i-1] == '*':
                    round[i] *= 2
            round[i] *= -1

    answer = sum(round)
    return answer
