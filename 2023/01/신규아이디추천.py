# https://school.programmers.co.kr/learn/courses/30/lessons/72410 골치아픈문제
# 정규표현식에 대해 공부한시간

# 이거 틀린코드임 다시풀어봐야됨
import re
def solution(new_id):
    answer = ''
    new_id = new_id.lower() #1
    new_id = re.sub(r"[^0-9^a-z^-^_^.]", '', new_id) #2
    if new_id == '':
        new_id = 'a' 
    new_id = re.sub('(([.])\\2{1,})', '.', new_id) #3
    if new_id == '':
        new_id = 'a' 
    if new_id[0] == '.':
        new_id = new_id[1:]
    if new_id == '':
        new_id = 'a' 
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:14]
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    return new_id


 # 다시푼코드
  
  

# [정규표현식](https://wikidocs.net/4308)
