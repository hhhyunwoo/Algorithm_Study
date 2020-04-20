#15686 삼성기출 치킨 배달
from itertools import combinations

if __name__ == "__main__":
    N,M = map(int,input().split())
    MAP = [list(map(int,input().split())) for _ in range(N)]
    chicken = list()
    house = list()
    for y in range(0,N):
        for x in range(0,N):
            if MAP[y][x] == 1:
                house.append((y,x))
            elif MAP[y][x] == 2:
                chicken.append((y,x))

    answer = 999999
    for p in range(1,M+1):
        for val in combinations(chicken,p):
            total_distance = 0
            for i in range(0,len(house)):
                MIN = 9999999
                for j in range(0,len(val)): #치킨 거리 최소값
                    distance = abs(house[i][0] - val[j][0])+abs(house[i][1] - val[j][1])
                    if distance < MIN:
                        MIN = distance
                total_distance += MIN
            answer = min(total_distance,answer)
    
    print(answer)