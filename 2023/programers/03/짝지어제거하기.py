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


