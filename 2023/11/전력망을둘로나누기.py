# https://school.programmers.co.kr/learn/courses/30/lessons/86971
import copy

def addEl(key, val):
    if key not in mesh:
        mesh[key] = []
    mesh[key].append(val)
    
mesh = {}
def solution(n, wires):
    answer = 9999999
    for node in wires:
        addEl(node[0], node[1])
        addEl(node[1], node[0])
        
    for i in range(len(wires)):
        cut = wires[i]
        if mesh[cut[0]] == []: 
            continue
            
        cMesh = copy.deepcopy(mesh)
        cMesh[cut[0]].remove(cut[1])
        cMesh[cut[1]].remove(cut[0])
        
        stack = [1]
        visit = [1]
        cnt = 0
        while stack:
            n = stack.pop()
            cnt += 1
            for node in cMesh[n]:
                if node not in visit:
                    stack.append(node)
                    visit.append(node)
                    
        comp = len(mesh)-cnt
        answer = min(answer, abs(comp-cnt))
        
    return answer
