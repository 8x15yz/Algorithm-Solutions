# https://www.acmicpc.net/problem/4358

# 이거외틇림 ..!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# import sys
# sys.stdin = open('test.txt', 'r')

trie = {}
cntAll = 0
while True:
    try:
        pointer = trie
        for word in input():
            if word not in pointer:
                pointer[word] = {}
            pointer = pointer[word]
        else: 
            if "cnt" not in pointer: pointer["cnt"] = 1
            else: pointer["cnt"] += 1
            cntAll += 1
    except EOFError:
        break


def getTree(pointer, treeName):
    if "cnt" in pointer:
        print(treeName, round(pointer["cnt"]/cntAll*100, 4)) #  소수점 4째자리까지 반올림해 
        return 
    
    for key in sorted(pointer.keys()):
        treeName += key                 # 문자 추가해서
        getTree(pointer[key], treeName) # 함수호출하고
        treeName = treeName[:-1]        # 넣었던 문자 다시 빼기
    
getTree(trie, "")
