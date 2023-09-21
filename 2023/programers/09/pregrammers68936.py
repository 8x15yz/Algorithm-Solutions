#https://school.programmers.co.kr/learn/courses/30/lessons/68936

## 이런 엉성한 코드가 93점짜리라니 ..
answer = []
zero, one = 0, 0
def solution(arr):
    global zero, one
    l = len(arr)
    if l == 1: return 
    else:
        quardList = [(0, l//2, 0, l//2),
                    (0, l//2, l//2,l),
                    (l//2,l, 0, l//2),
                    (l//2,l, l//2,l)]
        for a1, b1, a2, b2 in quardList: 
            newArr = []
            cnt = 0
            for i in range(a1, b1):
                inner = []
                for j in range(a2, b2):
                    inner.append(arr[i][j])
                    cnt += arr[i][j]
                newArr.append(inner)

            if cnt == (l//2)**2: 
                one += 1
                continue
            elif cnt == 0: 
                zero += 1
                continue
            solution(newArr)
    return [zero, one]
            
