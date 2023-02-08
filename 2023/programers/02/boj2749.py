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

# 틀린코드
N = int(input())
# 재귀함수 써보기
# 재귀함수로는 최대깊이 도달에러 남 = 쓰면 안된다는 뜻
def fibbo(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibbo(n-1)+fibbo(n-2)

print(fibbo(N))

# 귀납법으로 짠 코드
N = int(input())
fm = [[1, 1], [1, 0]]
fma = [[1, 1], [1, 0]]
for _ in range(N - 3):
    fmans = [[0, 0], [0, 0]]
    fmans[0][0] = (fma[0][0]*fm[0][0]) + (fma[0][1]*fm[1][0])
    fmans[0][1] = (fma[0][0]*fm[0][1]) + (fma[0][1]*fm[1][1])
    fmans[1][0] = (fma[1][0]*fm[0][0]) + (fma[1][1]*fm[1][0])
    fmans[1][1] = (fma[1][0]*fm[0][1]) + (fma[1][1]*fm[1][1])
    fma = fmans

print(sum(fmans[0]))
# 인데도 시간초과났음 ..

# 문제를 잘못읽엇다
# 파사노주기를 이용을 꼭 해야되는 거였음
N = int(input())
N %= 1000000
fm = [[1, 1], [1, 0]]
fma = [[1, 1], [1, 0]]
for _ in range(N - 3):
    fmans = [[0, 0], [0, 0]]
    fmans[0][0] = (fma[0][0]*fm[0][0]) + (fma[0][1]*fm[1][0])
    fmans[0][1] = (fma[0][0]*fm[0][1]) + (fma[0][1]*fm[1][1])
    fmans[1][0] = (fma[1][0]*fm[0][0]) + (fma[1][1]*fm[1][0])
    fmans[1][1] = (fma[1][0]*fm[0][1]) + (fma[1][1]*fm[1][1])
    fma = fmans

print(sum(fmans[0])%1000000)

#일단 행렬곱을 반복문으로만 돌린 버전 => 시간초과 났음



# 행렬곱연산을 재귀로 만들어서 통과
def power(baseMtrx, matrix):
    rstMtrx = [[0, 0], [0, 0]]
    rstMtrx[0][0] = (matrix[0][0] * baseMtrx[0][0]) + (matrix[0][1] * baseMtrx[1][0])
    rstMtrx[0][1] = (matrix[0][0] * baseMtrx[0][1]) + (matrix[0][1] * baseMtrx[1][1])
    rstMtrx[1][0] = (matrix[1][0] * baseMtrx[0][0]) + (matrix[1][1] * baseMtrx[1][0])
    rstMtrx[1][1] = (matrix[1][0] * baseMtrx[0][1]) + (matrix[1][1] * baseMtrx[1][1])
    # 65 - 68 코드는 다음과도 같이 작성할 수 있음 
    #for i in range(2):
    #    for j in range(2):
    #        for k in range(2):
    #            rstMtrx[i][j] += (matrix[i][k] * baseMtrx[k][j])
    return rstMtrx


def multiply(baseMtrx, B):
    if B == 1:
        return baseMtrx

    elif B % 2:
        matrix = multiply(baseMtrx, B - 1)
        rtnMtrx = power(baseMtrx, matrix)
        return rtnMtrx

    else:
        matrix = multiply(baseMtrx, B // 2)
        rtnMtrx = power(matrix, matrix)
        return rtnMtrx


N = int(input())
baseMtrx = [[1, 1], [1, 0]]
result = multiply(baseMtrx, N % 1500000)
print(result[0][1] % 1000000)
