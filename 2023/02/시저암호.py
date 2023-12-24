#https://school.programmers.co.kr/learn/courses/30/lessons/12926
def solution(s, n):
    answer = ''
    alpha = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,
            'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,
            'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    alphalist = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in s:
        if i == ' ':
            answer += ' '
        elif not i.islower():
            if alpha[i.lower()]+n >26:
                answer += alphalist[alpha[i.lower()]+n-26].upper()
            else:
                answer += alphalist[alpha[i.lower()]+n].upper()
        else:
            if alpha[i.lower()]+n >26:
                answer += alphalist[alpha[i]+n-26]
            else:
                answer += alphalist[alpha[i]+n]
            
    return answer
