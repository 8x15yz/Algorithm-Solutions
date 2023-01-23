# https://school.programmers.co.kr/learn/courses/30/lessons/131128

## 시간초과 코드
def solution(X, Y):
    answer = ''
    ans = []
    Xlist = []
    Ylist = []
    for x in X:
        Xlist.append(x)
    for y in Y:
        Ylist.append(y)
    
    for xl in range(len(Xlist)):
        for yl in range(len(Ylist)):
            if Xlist[xl] != 'x' and Xlist[xl] == Ylist[yl]:
                ans.append(int(Xlist[xl]))     
                Xlist[xl], Ylist[yl] = 'x', 'x'

    for i in sorted(ans, reverse=True):
        answer += str(i)
    for i in answer:
        if i != '0':
            break
    else:
        answer = '0'  
    if ans == []:
        answer = '-1'
        
    return answer
  
  
  
  ## 리팩토링 + 시간초과
  def solution(X, Y):
    answer = ''
    ans = []
    for x in X:
        if x in Y:
            Y = Y[:Y.index(x)] + Y[Y.index(x)+1:]
            ans.append(int(x))
    if ans == []:
        answer = '-1'
    else:
        for i in ans:
            if i != 0:
                for j in sorted(ans, reverse=True):
                    answer += str(j)
                break
        else:
             answer = '0'
    
    return answer
  
  
  ## 인덱스처리방법으로 리팩토링 + 시간초과
  def solution(X, Y):
    answer = ''
    ans = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in X:
        if x in Y:
            Y = Y[:Y.index(x)] + Y[Y.index(x)+1:]
            ans[int(x)] += 1
            
    if sum(ans) == 0:
        answer = '-1'
    elif sum(ans[1:]) == 0 and ans[0] > 0:
        answer = '0'
    else:
        for j in range(9, -1, -1):
                answer += str(j)*ans[j]
    
    return answer
  
  ## 정답코드
  ## x의 원소와 y의 원소를 일일이 대조하는 방법이 틀렸음 => 각 숫자를 카운트하는 방법으로 변경
  def solution(X, Y):
    answer = ''
    ans = 0
    for i in range(9, -1, -1):
        xc = X.count(str(i))
        yc = Y.count(str(i))
        if xc != 0 and yc != 0:
            answer += str(i)*(max(xc, yc)-abs(xc-yc)) 
            ans += i*(max(xc, yc)-abs(xc-yc)) 
            
    if answer == "":
        answer = '-1'
    elif ans == 0:
        answer = '0'
        
    return answer
