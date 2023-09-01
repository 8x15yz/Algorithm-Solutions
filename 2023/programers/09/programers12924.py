# https://school.programmers.co.kr/learn/courses/30/lessons/12924 
# 숫자의 표현
# set의 원소로 list 는 안들어간다는거 ~~~
# 기본테스트는 다맞았는데 효율성테스트에서 빵점임 ㅠㅠ 시간초과줄여야댐

def solution(n):
    visitSet = set()
    for k in range(1, n+1):
        visit = [i for i in range(k, n+1)]
        def compute(visit):
            while visit:
                Finn = 0
                finList = []
                while visit:
                    if Finn == n:  return tuple(finList)
                    now = visit[0]
                    if Finn + now <= n:
                        Finn += visit.pop(0)
                        finList.append(now)
                    else: return 0
        mid = compute(visit)
        if mid == 0: continue
        else: visitSet.add(mid)
        
    return len(visitSet)


## 이게 정해코드라고함 ~ 이거 보니까 내 코드 시갖초과 날만하다
def solution(n):
    count = 1
    for j in range(1,n):
        m1 = j
        while True:
            if j == n:
                count += 1
                break
            elif j > n:
                break
            m1 += 1
            j += m1

    return count
