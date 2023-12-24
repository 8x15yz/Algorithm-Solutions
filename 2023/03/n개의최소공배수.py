# https://school.programmers.co.kr/learn/courses/30/lessons/12953

## 시간초과 코드 ..
def solution(arr):
    answer = 1
    comblist = [[] for _ in range(4)]
    prime = [2, 3, 5, 7]
    
    for number in arr:
        primelist = {2:0, 3:0, 5:0, 7:0}
        num = number
        # 소수들로만 이루어진 조합 리스트를 만들기
        while num != 1:
            for i in prime:
                if num%i == 0:
                    num //= i
                    # comb += str(i)
                    primelist[i] += 1
                else:
                    continue
        for s in range(4):
            comblist[s].append(primelist[prime[s]])
    
    for c in range(4):
        answer *= prime[c]**max(comblist[c])
    return answer
  
  
## 
