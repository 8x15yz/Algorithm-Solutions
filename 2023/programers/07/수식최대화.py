#https://school.programmers.co.kr/learn/courses/30/lessons/67257

def calculate(a, b, cal):
    if cal == "*": return a*b
    elif cal == "+": return a+b
    else cal == "-": return a-b
    
from itertools import permutations

def solution(expression):
    calset = list(permutations(["+", "-", "*"], 3))
    for cal in calset:
        for c in cal:
            num = ""
            for e in range(len(expression)):
                if expression[e] == c:
                    backward, forward = "", ""
                    for j in range(e+1, len(expression)):
                        if not e.isdigit():
                            forward = str(calculate(int(num), backward, c))
                            break
                        else: backward += expression[e]
                elif not e.isdigit(): num = ""
                    
                    
             
    return answer
