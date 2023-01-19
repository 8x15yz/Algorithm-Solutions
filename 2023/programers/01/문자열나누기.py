# https://school.programmers.co.kr/learn/courses/30/lessons/140108
# 1시간

def solution(s):
    answer, same, diff = 0, 0, 0
    letter = s
    flag = 0
    ans = []
    while flag == 0:
        for i in range(len(letter)):
            if letter[0] == letter[i]:
                same += 1
            else:
                diff += 1
            if same == diff and same > 0:
                ans.append(letter[:i+1])
                letter = letter[i+1:]
                same, diff = 0, 0
                break
        else:
            if letter != '':
                ans.append(letter)
            flag = 1
    print(ans)
    answer = len(ans)
                
    return answer
