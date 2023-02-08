#  dp 공부 - 피보나치 수
N = int(input())
fib = [0, 1]
for i in range(N):
    fib.append(fib[i]+fib[i+1])
print(fib[-1])
