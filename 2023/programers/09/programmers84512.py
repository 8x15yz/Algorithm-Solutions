# https://school.programmers.co.kr/learn/courses/30/lessons/84512

words = {"A":0, "E":1, "I":2, "O":3, "U":4}

def solution(word):
    answer, exp, W = 0, 1, len(word)
    for _ in range(4): exp = (exp*5)+1
    
    for j in range(W):
        print(exp, words[word[j]], word[j], answer)
        answer += exp * words[word[j]]
        exp = exp//5
        
    print(answer)
    return answer + len(word)
