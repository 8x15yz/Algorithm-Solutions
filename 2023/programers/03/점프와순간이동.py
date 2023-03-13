# https://school.programmers.co.kr/learn/courses/30/lessons/12980
def solution(n):
    ans = 0
    # 이거 dp => 점화식을 만들어야됨
    dp = [0, 1, 1, 2, 1]
    if n <= 4:
        ans = dp[n]
    else:
        for i in range(5, n+1):
            if i%2 == 0:
                dp.append(dp[i//2])
            else:
                dp.append(dp[i-1]+1)
        ans = dp[-1]
    return ans
 
## 시간초과함 .. 아놔
## append 때문에 시갖초과되는듯 이거 없앨 생각을 해봐야겟음
## 정답코드

