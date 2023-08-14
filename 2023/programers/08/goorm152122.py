# https://level.goorm.io/exam/152122/현대모비스-본선-플레이리스트-만들기

# 트라이 공부중
#trie를 try중 ~ 찡긋
# N, K = map(int, input().split())
# for _ in range(N):
#     letter, minu = input().split()

trie = {"0":{}}
letters = ["liveforever", "liveyoung", "happening", "happyending"]
for letter in letters:
    pointer = trie["0"]
    for l in letter:
        if l not in pointer:
            pointer[l] = {}
        pointer = pointer[l]
print(trie)
