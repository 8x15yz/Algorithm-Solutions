N, K = map(int, input().split())
arr = [float('inf') for _ in range(int(1e5)+1)]

queue = [(N, 0)]
while queue:
    ssum, cnt = queue.pop(0)
    if ssum == K:
        if arr[K] == float('inf'):
            print(0)
        else:
            print(cnt)
        break
    if 0 <= ssum+1 <= 1e5 and arr[ssum+1] > cnt:
        queue.append((ssum+1, cnt + 1))
        arr[ssum+1] = cnt

    if 0 <= ssum-1 <= 1e5  and arr[ssum-1] > cnt:
        queue.append((ssum-1, cnt + 1))
        arr[ssum-1] = cnt

    if 0 <= ssum*2 <= 1e5  and arr[ssum*2] > cnt:
        queue.append((ssum*2, cnt + 1))
        arr[ssum*2] = cnt