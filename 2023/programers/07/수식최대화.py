# https://school.programmers.co.kr/learn/courses/30/lessons/67257
# 진짜드럽게풀엇음 ..
# 근데 다들 드럽게 풀긴 했네 ㅋㅋㅋㅋ

def cal(a, b, cal):
    if cal == "-": return str(int(a)-int(b))
    elif cal == "*": return str(int(a)*int(b))
    else: return str(int(a)+int(b))

from itertools import permutations
def solution(source):
    maxnum = 0
    for calset in list(permutations(["-", "+", "*"], 3)):
        exp = source + ')'
        for c in calset:
            lenexp = len(exp)
            answer = 0
            i = 0
            newexp = ''
            num = ""
            while i < lenexp:
                if num != "" and exp[i] == c: 
                    forward = num
                    num = ""
                    j = i+1
                    while j < lenexp:
                        if num != "" and not exp[j].isdigit():
                            backward = num
                            num = cal(forward, backward, c)
                            i = j-1
                            break
                        else: num += exp[j]
                        j += 1
                elif num != "" and not exp[i].isdigit():
                    newexp += num + exp[i]
                    num = ""
                else: num += exp[i]

                i += 1
            exp = newexp
        else:
            if maxnum < abs(int(newexp[:-1])): maxnum = abs(int(newexp[:-1]))
    return maxnum
