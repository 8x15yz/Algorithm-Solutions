# https://school.programmers.co.kr/learn/courses/30/lessons/12915

#틀린코드
# bubble sort 사용하기
def solution(strings, n):
    answer = []
    alpha = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,
            'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,
            'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    ls = len(strings)-1
    for i in range(ls):
        for j in range(ls-i):
            m = n
            while m != len(strings[j]):
                if alpha[strings[j][m]] > alpha[strings[j+1][m]]:
                    strings[j], strings[j+1] = strings[j+1], strings[j]
                    break
                elif alpha[strings[j][m]] == alpha[strings[j+1][m]]:
                    m += 1
                else:
                    break
    return strings
  
  
# n번째 문자가 같으면 "사전순"으로 정렬 (바로 다음 문자부터 비교하는게 아니라)
# bubble sort 사용하기
def solution(strings, n):
    answer = []
    alpha = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,
            'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,
            'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    ls = len(strings)-1
    for i in range(ls):
        for j in range(ls-i):
            if alpha[strings[j][n]] > alpha[strings[j+1][n]]:
                    strings[j], strings[j+1] = strings[j+1], strings[j]
            elif alpha[strings[j][n]] == alpha[strings[j+1][n]]:
                    m = 0
                    while m != len(strings[j]):
                        if alpha[strings[j][m]] > alpha[strings[j+1][m]]:
                            strings[j], strings[j+1] = strings[j+1], strings[j]
                        elif alpha[strings[j][m]] == alpha[strings[j+1][m]]:
                            m += 1
                        else:
                            break
    return strings
