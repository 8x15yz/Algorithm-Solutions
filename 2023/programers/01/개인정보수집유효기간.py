# https://school.programmers.co.kr/learn/courses/30/lessons/150370?language=python3
# 12시 ~ 3시 (3시간)

def solution(today, terms, privacies):
    answer = []
    tdyr, tdmt, tddy = int(today[:4]), int(today[5:7]), int(today[-2:])
    term = {}
    privlist = []
    for trm in terms:
        term[trm[:1]] = int(trm[2:])
    for piv in privacies:
        privlist.append((piv[-1:], int(piv[:4]), int(piv[5:7]), int(piv[8:10])))
    cnt = 0
    for piv, pivyr, pivmt, pivdy in privlist:
        cnt += 1
        if tdyr == pivyr:
            tdrg = (tdmt*28+tddy)-(pivmt*28+pivdy)
            pivrg = term[piv]*28
            if tdrg >= pivrg:
                answer.append(cnt)
        if tdyr > pivyr:
            tdrg = ((tdyr-pivyr)*12*28)+(tdmt*28+tddy)-(pivmt*28+pivdy)
            pivrg = term[piv]*28
            if tdrg >= pivrg:
                answer.append(cnt)
            
                
    return answer
