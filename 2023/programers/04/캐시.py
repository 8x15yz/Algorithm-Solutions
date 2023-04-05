# https://school.programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    answer = 5
    cache = [cities.pop(0)]
    
    for page in cities:
        # print(page, cache, end='')
        if page in cache:
            cache.remove(page)
            cache = [page]+cache
            answer += 1
            # print(1)
        else:
            cache = [page]+cache[:cacheSize-1]
            answer += 5
            # print(5)
    
    return answer


# cache 사이즈가 0인 경우의 예외처리 + 도시명을 모두 lowercase로 변형해 적용한 정답코드
def solution(cacheSize, cities):
    if cacheSize == 0: 
        return len(cities)*5
    
    else:
        answer = 5
        cache = [cities.pop(0).lower()]

        for page in cities:
            page = page.lower()
            if page in cache:
                cache.remove(page)
                cache = [page]+cache
                answer += 1
            else:
                cache = [page]+cache[:cacheSize-1]
                answer += 5
        return answer
