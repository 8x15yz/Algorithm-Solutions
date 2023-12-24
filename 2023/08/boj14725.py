# https://www.acmicpc.net/problem/14725
trie = {}

for _ in range(int(input())):
    front = ""
    fromAnt = list(input().split())
    pointer = trie
    for i in range(1, int(fromAnt[0])+1):
        newKey = front+fromAnt[i]
        if not newKey in pointer:
            pointer[newKey] = {}
        pointer = pointer[newKey]
        front += "--"

def unpack(pointer):
    if pointer == {}: return 
    for key in sorted(pointer.keys()):
        print(key)
        unpack(pointer[key])
unpack(trie)
