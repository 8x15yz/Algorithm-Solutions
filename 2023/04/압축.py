# https://school.programmers.co.kr/learn/courses/30/lessons/17684

# 앜ㅋ 너무쉽죠?
def solution(msg):
    answer = []
    messageD = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 
                'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 
                'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    lastDNumber = 27
    i = 0
    while i < len(msg):
        if msg[i] in messageD:
            pointer = i+2
            while True:
                if msg[i:pointer] in messageD:
                    if pointer > len(msg):
                        return (answer+[messageD[msg[i:pointer]]])
                    pointer += 1
                else:
                    answer.append(messageD[msg[i:pointer-1]])
                    messageD[msg[i:pointer]] = lastDNumber
                    lastDNumber += 1
                    i = pointer-1
                    break
    return answer
