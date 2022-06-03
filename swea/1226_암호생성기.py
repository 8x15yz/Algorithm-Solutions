# import sys
# sys.stdin = open('1225ans.txt', 'r')

for _ in range(1, 11):
    tc = int(input())
    queue = list(map(int, input().split()))

    endFlag = 0
    while endFlag == 0:
        for i in range(1, 6):
            cell = queue.pop(0) - i
            if cell <= 0:
                queue.append(0)
                endFlag = 1
                break
            queue.append(cell)

    print('#{}'.format(tc), *queue)
