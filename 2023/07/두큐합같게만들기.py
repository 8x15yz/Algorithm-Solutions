# https://school.programmers.co.kr/learn/courses/30/lessons/118667

def solution(queue1, queue2):
    answer = 0
    st = len(queue1)
    queue1 += queue2
    end = len(queue1)-1
    goal = sum(queue1)//2
    state = sum(queue2)
    while answer < 1000000:
        if state == goal:
            return answer
        elif state > goal:
            state -= queue1[st]
            st = (st+1)%len(queue1)
        else:
            end = (end+1)%len(queue1)
            state += queue1[end]
        answer += 1
        
    
    return -1


# 음 .. 정말 못생긴 코드인데 일단 풀렸다
# pop append를 쓰면 1000000 돌릴때 시간초과나서 그걸 안쓰고 
# 인덱스 정보를 활용하는 방법으로 만드니까 1000000번 돌려도 시간초과가 안나게 하는 쪽으로 해결
