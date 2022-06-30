N = int(input())
inputarr = [list(map(int, input().split())) for _ in range(N)]

def dice(face, arr, seq):
    if arr[seq].index(face)%2 == 0:
        facedidx = arr[seq].index(face)+1
    else:
        facedidx = arr[seq].index(face) -1
    faced = arr[seq][facedidx]
    return faced

arr = [[0, 0, 0, 0, 0, 0] for _ in range(N)]


for i in range(N):
    arr[i][0] = inputarr[i][0]
    arr[i][1] = inputarr[i][5]
    arr[i][2] = inputarr[i][1]
    arr[i][3] = inputarr[i][3]
    arr[i][4] = inputarr[i][2]
    arr[i][5] = inputarr[i][4]

answer = []
for g in range(6):
    visit = [[0, 0, 0, 0, 0, 0] for _ in range(N)]
    faced = arr[0][g]
    visit[0][g] = 1
    for i in range(N-1):
        faced = dice(faced, arr, i)
        visit[i][arr[i].index(faced)] =1
        visit[i+1][arr[i+1].index(faced)] =1
    faced = dice(faced, arr, N-1)
    visit[N-1][arr[N-1].index(faced)] = 1

    # print(visit)
    track = []
    for i in range(len(visit)):
        inarr = []
        for j in range(len(visit[i])):
            if visit[i][j] == 0:
                inarr.append(arr[i][j])
        track.append(inarr)
    ans = 0
    for i in range(len(track)):
        ans += max(track[i])
    answer.append(ans)

print(max(answer))