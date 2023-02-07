# https://school.programmers.co.kr/learn/courses/30/lessons/12939
# 테케는 다 맞는데 왜 채점은 0점임'
def solution(s):
    answer = ''
    s = list(s+' ')
    news = []
    flag = 0
    wc = 0
    while wc != len(s):
        if s[wc] == ' ':
            if s[flag:wc][0] == '-':
                news.append(-1*int(s[flag:wc][1]))
            else:
                news.append(int(s[flag:wc][0]))
            flag = wc+1
        wc += 1
            
    answer = str(min(news)) + ' ' + str(max(news))
    return answer


#  당연함 바보라서 그럼
def solution(s):
    answer = ''
    s = list(s+' ')
    news = []
    flag = 0
    wc = 0
    while wc != len(s):
        if s[wc] == ' ':
            if s[flag:wc][0] == '-':
                news.append(-1*int(''.join(s[flag+1:wc])))
            else:
                news.append(int(''.join(s[flag:wc])))
            flag = wc+1
        wc += 1
            
    answer = str(min(news)) + ' ' + str(max(news))
    return answer
