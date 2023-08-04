# https://school.programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = ''
    ins_id = new_id
    ins_id = ins_id.lower()

    takeOut = ""
    for i in ins_id:
        if i.isalpha() or i.isdigit() or i in ["-", "_", "."]:
            takeOut += i
    ins_id = takeOut

    flag = 0
    takeOut = ""
    for i in ins_id:
        if i == "." and flag == 0:flag = 1
        elif i == "." and flag == 1: continue
        elif flag == 1 and i != ".": flag = 0
        takeOut += i
    ins_id = takeOut

    takeOut = ""
    for i in range(len(ins_id)):
        if i == 0 or i == len(ins_id)-1:
            if ins_id[i] == ".": continue
        takeOut += ins_id[i]
    ins_id = takeOut
    
    if ins_id == "": ins_id = "a"

    takeOut = ""
    if len(ins_id) >= 15: ins_id = ins_id[:15]

    if ins_id[-1] == "." : ins_id = ins_id[:-1]

    lenid = len(ins_id)
    while lenid <= 2:
        ins_id += ins_id[-1]
        lenid = len(ins_id)
        
    return ins_id
