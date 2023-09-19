# https://school.programmers.co.kr/learn/courses/30/lessons/131704


## 첫번째 시도
def solution(order):
    answer = 0
    press = [i for i in range(1, len(order)+1)]
    stack = [press.pop(0)]
  
    while press:
      stack.append(press.pop(0))
      
        while stack and stack[-1] == order[0]:
            answer += 1
            order.pop(0)
            stack.pop()
        
    return answer



## 두번째 시도
def solution(order):
    answer = 0
    press = [i for i in range(1, len(order)+1)]
    stack = []
            
    for i in range(1, len(order)+1):
        stack.append(i)
        
        while stack and stack[-1] == order[0]:
            answer += 1
            stack.pop()
            order.pop(0)
            
    return answer


## 정답코드
def solution(order):
    answer = 0
    press = [i for i in range(1, len(order)+1)]
    stack = []
    id = 0
    for i in range(1, len(order)+1):
        stack.append(i)
        
        while stack and stack[-1] == order[id]:
            answer += 1
            stack.pop()
            id += 1
            
    return answer
