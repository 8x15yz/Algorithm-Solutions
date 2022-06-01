for tc in range(1, 11):
    T = int(input())
    arr = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]

    for i in range(102):
        if arr[99][i] == 2:
            hori = i
    ver = 99
    up = [-1, 0, 0]
    lr = [0, -1, 1]
    while ver !=0 :
        for i in range(3):
            if arr[ver+up[i]][hori+lr[i]] == 1:
                arr[ver][hori] = 0
                ver, hori = ver+up[i], hori+lr[i]
    print('#{} {}'.format(tc, hori-1))