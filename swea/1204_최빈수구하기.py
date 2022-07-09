#import sys
#sys.stdin = open('swea1204.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    Tnum = int(input())
    arr = list(map(int, input().split()))
    count = [0]*101

    for ct in arr:
        count[ct] += 1
    ans = []
    # print(max(count), count)
    for i in range(101):
        if count[i] == max(count):
            ans.append(i)
    print('#{} {}'.format(tc, max(ans)))
    
    
# 0 ~ 100 까지의 인덱스를 가진 배열을 생성하고 (count)
# 수 리스트를 arr 로 입력받아서 각 숫자에 해당하는 인덱스에 1을 누적하였습니다
# 최빈수가 여러개일 수 있으므로 ans 배열을 만들고 
# count를 한번씩 돌면서 ⇒ count의 최댓값에 해당한다면 ans 배열에 append
# count 까지도 모두 돌았다면 ans의 최댓값을 출력하도록 하였습니다.

