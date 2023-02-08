# 틀린코드 ..
N = int(input())
# boj 2749 = 메모리 효율을 고려해야됨
# fib 리스트 앞쪽의 원소를 없애는것도 나쁘지 않음
fib0, fibn1 = 0, 1
fibn = 0
for i in range(N-1):
  fibn = fib0 + fibn1
  fibn1, fib0 = fibn, fibn1

print(fibn)


# 정답코드

