# https://school.programmers.co.kr/learn/courses/30/lessons/12985
#아니 이거 뭐임..? 
def solution(t,a,b):
    answer = 0
    # 이진탐색으로 풀기
    al, ar, bl, br, n, cnt = 0, t, 0, t, t, 0
    while True:
        cnt += 1
        n //= 2
        print(n)
        # ar, al = (ar, n+al) if n > a else (ar-n, al)
        if n > a:
            ar, al = ar-n, al
        else:
            ar, al = ar, al+n+1
            
        # br, bl = (br, n+bl) if n > b else (br-n, bl)
        if n > b:
            br, bl = br-n, bl
        else:
            br, bl = br, bl+n+1
        print(ar, al, br, bl)
        if al != bl or ar != br or n == 1:
            print(cnt)
            break
    return answer

  
  # 또틀림
def solution(t,a,b):
    answer = 0
    # 이진탐색으로 풀기
    al, ar, bl, br, n, cnt = 0, t, 0, t, t, 0
    while True:
        cnt += 1
        n //= 2
        if n >= a:
            ar, al = ar-n, al
        else:
            ar, al = ar, al+n+1
        if n >= b:
            br, bl = br-n, bl
        else:
            br, bl = br, bl+n+1
            
        if al != bl or ar != br or n == 1:
            break
    for i in range(t//2):
        if 2**i == t:
            answer = i-cnt+1
    return answer


## 정답코드
def solution(n,a,b):
    answer = 0
    # 각각 루트 노드를 찾고 둘의 공통된 루트 노드의 레벨을 찾는건 어때
    # 포화이진트리라고 가정하고 
    t, lev, nodes = n, 0, n
    while t!=1:
        t //= 2
        nodes += t
        lev += 1
    nodea, nodeb = nodes-n+a, nodes-n+b
    while nodea != nodeb:
        answer += 1
        nodea //= 2
        nodeb //= 2
    return answer
