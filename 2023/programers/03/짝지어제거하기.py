#
# 이거 골치아픈 문제네 ..
# 틀린코드
def solution(s):
    answer = 0
    i = 0
    while True:
        slen = len(s)
        if s == '':
            answer = 1
            break
        elif len(s) == 1:
            answer = 0
            break
            
        if i == slen:
            i = 0
            continue
            
        if s[i] == s[i+1]:
            s = s[:i]+s[i+2:]
        i += 1
        
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                break
        else:
            answer = 0
            break
            
    return answer

# 어디서 오타나는지는 알았는데 이제는 시간초과 코드
def solution(s):
    answer = 0
    i = 0
    while True:
        slen = len(s)
        if s == '':
            answer = 1
            break
        elif len(s) == 1:
            answer = 0
            break
            
        if i == slen:
            i = 0
            continue
            
        if s[i] == s[i+1]:
            s = s[:i]+s[i+2:]
            # replace 또는 [:index]+[index+2:]를 사용하면 문자열 일부를 훑기때문에 효율성 테스트에서 실패합니다.
            # 진짜 명치맞음ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
        i += 1
        
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                break
        else:
            if s == '':
                answer = 1
            else:
                answer = 0
            break
            
    return answer


# 스택으로 기본케이스 다 풀렸는데 효율성에서 막힘 
def solution(s):
    answer = 0
    s = list(s)
    stack = [s.pop(0)]
    while s:
        a = s.pop(0)
        if stack and a == stack[-1]:
            stack.pop()
        else:
            stack.append(a)
    answer = 0 if stack else 1
        
    return answer




