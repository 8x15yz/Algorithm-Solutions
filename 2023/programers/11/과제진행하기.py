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



def getTime(time):
    h, m = time.split(":")
    return int(h)*60+int(m)

def preprocess(plans):
    for plan in plans:
        plan[1], plan[2] = getTime(plan[1]), int(plan[2])
    plans.sort(key = lambda x : x[-2], reverse=True)
    return plans


def solution(plans):
    # plans = 
    answer = []
    later = []
    plans = preprocess(plans)
    while True:
        p = plans.pop()
        if not plans: 
            answer.append(p[0])
            break
        t, comp = p[1]+p[2], plans[-1][1]
        if t > comp:
            later.append([p[0], t-comp])
        elif t < comp:
            answer.append(p[0])
            while later:
                l = later.pop()
                if t+l[1] <= comp:
                    answer.append(l[0])
                    t += l[1]
                else:
                    l[1] = t+l[1]-comp
                    later.append(l)
                    break
        else:
            answer.append(p[0])
    while later:
        answer.append(later.pop()[0])

    return answer
