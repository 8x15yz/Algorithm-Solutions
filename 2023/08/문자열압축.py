#https://school.programmers.co.kr/learn/courses/30/lessons/60057

def intToStr(string):
    if string == 1: return ""
    else: return str(string)

def solution(s):
    lenS = len(s)
    compactions = {}
    for i in range(1, lenS):
        sample = []
        for j in range(0, lenS, i):
            letter = s[j:j+i]
            if len(letter) < i: sample[-1] += letter
            else: sample.append(s[j:j+i])
        compact = ""
        rep = sample.pop(0)
        cnt = 1
        for sam in sample:
            if sam == rep: cnt += 1
            else: 
                compact += intToStr(cnt)+rep
                rep, cnt = sam, 1
        else: compact += intToStr(cnt)+rep

        if compact == "": continue
        else: compactions[len(compact)] = compact
    
    return min(compactions)
