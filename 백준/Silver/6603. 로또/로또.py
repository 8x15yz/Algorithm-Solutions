def comb(p, r, n):
    if n == N:
        for i in p:
            print(arr[i], end=" ")
        print()
        return
    if len(p) == 0:
        smallest = 0
    else:
        smallest = p[-1]
    for i in range(smallest, r):
        if not i in p:
            p.append(i)
            comb(p, r, n+1)
            p.pop()

N = 6

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    k = arr.pop(0)
    comb([], k, 0)
    print()
