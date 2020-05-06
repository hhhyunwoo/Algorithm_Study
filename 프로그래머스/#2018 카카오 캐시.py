#2018 카카오 캐시

'''
LRU 사용하고 사용한 값을 맨 앞으로 당겨주는 것은 안해서 틀렸음.
LRU 공부해놓기
'''

import copy
from collections import Counter


def solution(cacheSize, cities):
    cache = []
    time = 0
    if cacheSize == 0:
        time = len(cities)*5
    else:
        for city in cities:
            if city.lower() in cache:
                tmp = cache[cache.index(city.lower())]
                cache.remove(tmp)
                cache.append(tmp)
                time += 1
            else:
                if len(cache)>= cacheSize:
                    cache.pop(0)
                cache.append(city.lower())
                time+=5
        
    return time

if __name__ == "__main__":
    print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))

