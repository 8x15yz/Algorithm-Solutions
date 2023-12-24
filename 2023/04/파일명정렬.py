# https://school.programmers.co.kr/learn/courses/30/lessons/17686

def solution(realfiles):
    files = realfiles.copy()
    answer = []
    # 1. 대소문자 정렬 > 2. 숫자 정렬 > 3. 위치하는 순서대로 정렬
    fileDict = {}
    for i in range(len(files)):
        view = files[i]
        splitInto, check = [], ''
        for j in range(len(view)):
            if j+1 != len(view): 
                if view[j].isdigit() == False and view[j+1].isdigit():
                    splitInto.append(str(check+view[j]).lower())
                    check = ''
                    fileDict[check+view[j]] = view
                elif view[j+1].isdigit() == False and view[j].isdigit():
                    splitInto.append(int(check+view[j]))
                    check = ''
                else: check += view[j]
        else: files[i] = splitInto[:2]+[i]

    files = sorted(files, key = lambda x: (x[0] , x[1]))

    
    for file in files: answer.append(realfiles[file[-1]])
    return answer



## 정답 => 바로 끊어주는것보다 인덱스를 가져와서 슬라이싱 해주는게 더 안전함
def solution(realfiles):
    files = realfiles.copy()
    answer = []
    fileDict = {}
    cnt = 0
    HeadTail = []
    for i in range(len(files)):
        view = files[i]
        for j in range(len(view)):
            if j+1 < len(view) and view[j].isdigit() != view[j+1].isdigit():
                HeadTail.append(j+1)
                cnt += 1
        else: 
            if len(HeadTail) == 1:
                files[i] = [view[:HeadTail[0]].lower(), int(view[HeadTail[0]:]), i]
            else:
                files[i] = [view[:HeadTail[0]].lower(), int(view[HeadTail[0]:HeadTail[1]]), i]
            cnt, HeadTail = 0, []

    files = sorted(files, key = lambda x: (x[0] , x[1]))
    for file in files: answer.append(realfiles[file[-1]])
    return answer
