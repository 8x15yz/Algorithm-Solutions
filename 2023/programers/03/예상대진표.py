# 
#아니 이거 뭐임..? 
def solution(t,a,b):
    answer = 0
    # 이진탐색으로 풀기
    al, ar, bl, br, n, cnt = 0, t, 0, t, t, 0
    while True:
        cnt += 1
        n //= 2
        print(n)
        # ar, al = (ar, n+al) if n > a else (ar-n, al)
        if n > a:
            ar, al = ar-n, al
        else:
            ar, al = ar, al+n+1
            
        # br, bl = (br, n+bl) if n > b else (br-n, bl)
        if n > b:
            br, bl = br-n, bl
        else:
            br, bl = br, bl+n+1
        print(ar, al, br, bl)
        if al != bl or ar != br or n == 1:
            print(cnt)
            break
    return answer
  
  # 머리 왜이렇게 안돌아가지??
