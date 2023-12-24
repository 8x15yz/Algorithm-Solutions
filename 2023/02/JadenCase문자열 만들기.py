# https://school.programmers.co.kr/learn/courses/30/lessons/12951
def solution(s):
    s = list(s)
    firstAlpha = 0
    for i in range(len(s)):
        if s[i].isalpha():
            if firstAlpha == 0:
                s[i] = s[i].upper()
                firstAlpha = 1
            else:
                s[i] = s[i].lower()
        elif s[i] == " ":
            firstAlpha = 0
        elif s[i].isnumeric():
            firstAlpha = 1
            
    return ''.join(s)
