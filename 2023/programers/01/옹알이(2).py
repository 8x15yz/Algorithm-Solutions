# https://school.programmers.co.kr/learn/courses/30/lessons/133499

def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]
    for wd in range(len(babbling)):
         for i in range(4):
                if word[i] in babbling[wd]:
                    babbling[wd] = babbling[wd].replace(word[i], str(i))
                    
    for wd in babbling:
        print(wd)
        for i in wd:
            if i !='0' and i !='1' and i !='2' and i !='3':
                break
        else:
            for i in range(len(wd)-1):
                if wd[i] == wd[i+1]:
                    break
            else:
                answer += 1
        
    return answer
