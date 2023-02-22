#https://school.programmers.co.kr/learn/courses/30/lessons/12909

# 틀린코드
def solution(s):
    s = list(s)
    answer = True
    stack = [s.pop(0)]
    while s:
        n = s.pop(0)
        if n == ')':
            stack.pop()
        else:
            stack.append(n)
    if stack == []:
        answer = True
    else:
        answer = False
    return answer
  
# 틀리고 있는 코드
# 이거 뭐임 .. 내가모르는 함정 뭐임 이거 
# 테케 자꾸 틀림 ..
def solution(s):
    s = list(s)
    answer = True
    stack = [s.pop(0)]
    while s:
        n = s.pop(0)
        if n == ')':
            if stack == []:
                break
            stack.pop()
        else:
            stack.append(n)
            
    print(s, stack)
    if stack == []:
        answer = True
    else:
        answer = False
    return answer
