# https://level.goorm.io/exam/152122/현대모비스-본선-플레이리스트-만들기

# 트라이 공부중

# 0816 수요일
import sys
sys.stdin = open('test.txt', 'r')

N, K = map(int, input().split())
letters = [tuple(input().split()) for _ in range(N)]
print(letters)

trie = {"0":{}}
for letter, minu in letters:
    pointer = trie["0"]
    for l in range(len(letter)):
        if l == len(letter)-1:
            pointer[letter[l]] = int(minu)
        elif letter[l] not in pointer:
            pointer[letter[l]] = {}
        pointer = pointer[letter[l]]

print(trie)
pointer = trie["0"]

def inToTrie(pointer, word, wlist):
    if type(pointer) == int: 
        print(word, pointer, wlist)
        return
    print(pointer, word)
    if len(pointer) >= 2: wlist.append(word)
    for key in pointer.keys():
        inToTrie(pointer[key], word+key, wlist)
    return wlist
ans = inToTrie(pointer, "", [])
print(ans)
# 트라이 만들고 단어 끝마다 런타임 달아주는 것까지 작성
# 이제 하고싶은 일은 접두사마다 런타임 구하는 로직 짜기
