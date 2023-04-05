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
