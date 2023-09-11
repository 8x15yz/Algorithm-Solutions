# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
## 당연히 틀리는코드 .. 

import sys
sys.stdin = open('test.txt', 'r')

for tc in range(1, int(input())+1):
  cards, n = input().split()
  cards, n = list(map(int, list(cards))), int(n)
  
  def selectionsort(cards, n):
    cl = len(cards)
    cnt = 0
    for i in range(cl):
      mCard, mDex = 0, 0
      for j in range(cl-1, i, -1):
        if mCard < cards[j]: mCard, mDex = cards[j], j
      else:
        if mCard > cards[i]: 
          cards[i], cards[mDex] = mCard, cards[i]
          cnt += 1
          if cnt == n: return cards
    return cards

  cards = selectionsort(cards, n)
  ans = 0
  for k in range(len(cards)):
    ans += cards[k]*(10**(len(cards)-k-1))
  print("#"+str(tc), ans)
