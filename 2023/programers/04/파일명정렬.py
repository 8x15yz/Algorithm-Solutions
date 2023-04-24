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
