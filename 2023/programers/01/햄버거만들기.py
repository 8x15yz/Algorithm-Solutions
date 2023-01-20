#https://school.programmers.co.kr/learn/courses/30/lessons/133502 지독한 문제 ..

## 시간초과 코드 (50점)
def solution(ingredient):
    #'1231'이 되는 문자열을 찾기
    answer = 0
    ing = ''
    for i in ingredient:
        ing += str(i)
        print(ing)
        while '1231' in ing:
            ing = ing.replace('1231', '')
            answer += 1
    return answer

## 시간초과 (55.6점)
def solution(ingredient):
    answer = 0
    stack = ingredient[:3]
    ing = ingredient[3:]
    for i in range(len(ing)):
        stack.append(ing.pop(0))
        if stack[-4:] == [1, 2, 3, 1]:
            stack = stack[:len(stack)-4]
            answer += 1
    
    return answer
  

## 시간초과 (50점, 문자열탐색 방법 풀이)
def solution(ingredient):
    answer = 0
    while True:
        for i in range(len(ingredient)-3):
            if ingredient[i:i+4] == [1, 2, 3, 1]:
                del ingredient[i:i+4]
                answer += 1
                break
        else:
            break
    return answer
  
  
## 정답코드 
## 문자열 탐색 풀이에서 탐색 시작 인덱스를 가지치기 하는 방법으로 해결
def solution(ingredient):
    answer = 0
    startidx = 0
    while True:
        for i in range(startidx, len(ingredient)-3):
            if ingredient[i:i+4] == [1, 2, 3, 1]:
                del ingredient[i:i+4]
                answer += 1
                startidx = i-2
                break
        else:
            break
    return answer
