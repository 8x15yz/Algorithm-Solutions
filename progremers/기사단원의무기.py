# 시간초과남
def solution(number, limit, power):
    answer = 0
    memo = [0]
    for person in range(1, number+1):
        # 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기
        # 제한 있음 => 제한 초과 무기는 협약기관에서 구매
        cnt = 0
        for i in range(len(memo), person+1):
            if person % i == 0:
                cnt += 1
        memo.append(cnt)
        if limit < cnt:
            answer += power
        else:
            answer += cnt

    return answer
