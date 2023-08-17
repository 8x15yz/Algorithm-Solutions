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
print(trie)

def unpack(pointers):
    if pointers == {}: return 
    for key in sorted(pointers.keys()):
        print(key)
        pointer = pointers[key]
        unpack(pointer)
unpack(trie)
