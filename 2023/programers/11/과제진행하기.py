# https://school.programmers.co.kr/learn/courses/30/lessons/176962

def getTime(time):
    h, m = time.split(":")
    return int(h)*60+int(m)

def preprocess(plans):
    for plan in plans:
        plan[1], plan[2] = getTime(plan[1]), int(plan[2])
    plans.sort(key = lambda x : x[-2])
    return plans

t = 0
def solution(plans):
    answer = []
    plans = preprocess(plans)
    while len(plans) > 1:
        p = plans.pop(0)
        t = p[1]
        while True:
            t += 1
            p[2] -= 1
            if p[2] == 0:
                answer.append(p[0])
                break
            if t == plans[0][1]:
                plans.append(p)
                break
    answer.append(plans[0][0])
    return answer

