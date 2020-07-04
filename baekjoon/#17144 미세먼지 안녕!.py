#17144 미세먼지 안녕!
import sys
from collections import deque
import copy
input=sys.stdin.readline
inf = 2*32

dy=[-1,1,0,0]
dx=[0,0,-1,1]

def spread():
    air_map=[[0 for _ in range(c)] for _ in range(r)]
    for y in range(0,r):
        for x in range(0,c):
            if MAP[y][x]>0:#미세먼지
                cnt=0
                for dir in range(0,4):
                    ny=y+dy[dir]
                    nx=x+dx[dir]
                    val=MAP[y][x]//5
                    if 0<=ny<r and 0<=nx<c and MAP[ny][nx]>=0:
                        cnt+=1
                        air_map[ny][nx]+=val
                air_map[y][x] += MAP[y][x]- val*cnt
    return air_map

r,c,t=map(int,input().split())
MAP=[list(map(int,input().split())) for _ in range(r)]
air=[]
for y in range(0,r):
    for x in range(0,c):
        if MAP[y][x]==-1:air.append(y)

for _ in range(t):
    tmp = spread()
    tmp[air[0]][0],tmp[air[1]][0]=-1,-1
    MAP=copy.deepcopy(tmp)

    MAP2=[[0 for _ in range(c)] for _ in range(r)]

    a = air[0]
    for j in range(1,c-1):
        MAP2[a][j+1] = MAP[a][j]
    MAP2[a-1][c-1] = MAP[a][c-1]
    for j in range(a,0,-1):
        MAP2[j-1][c-1] = MAP[j][c-1]
    MAP2[0][c-2]=MAP[0][c-1]
    for j in range(c-1,0,-1):
        MAP2[0][j-1] = MAP[0][j]
    MAP2[1][0] = MAP[0][0]
    for j in range(0,a-1):
        MAP2[j+1][0] = MAP[j][0]
    
    a = air[1]
    for j in range(1,c-1):
        MAP2[a][j+1] = MAP[a][j]
    MAP2[a+1][c-1] = MAP[a][c-1]
    for j in range(a,r-1):
        MAP2[j+1][c-1] = MAP[j][c-1]
    MAP2[r-1][c-2]=MAP[r-1][c-1]
    for j in range(c-1,0,-1):
        MAP2[r-1][j-1] = MAP[r-1][j]
    MAP2[r-2][0] = MAP[r-1][0]
    for j in range(r-1,a-1,-1):
        MAP2[j-1][0] = MAP[j][0]
    
    MAP2[air[0]][0],MAP2[air[1]][0]=-1,-1
    for y in range(1,air[0]):
        for x in range(1,c-1):
            MAP2[y][x]=MAP[y][x]
    for y in range(air[1]+1,r-1):
        for x in range(1,c-1):
            MAP2[y][x]=MAP[y][x]
    MAP=copy.deepcopy(MAP2)

SUM=2
for row in range(0,r):
    SUM+=sum(MAP[row])
print(SUM)