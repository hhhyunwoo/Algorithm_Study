#2146 다리 만들기

'''섬들 각각 1,2,... 로 색칠해야할듯?

사방에 0이 하나라도 있는지 체크
있다면 bfs돌려서 다른 섬 나올때까지 count하기'''

'''
와우,,
간척 사업을 한다,,,???

1.간척사업
1.1 한꺼번에 섬들의 너비를 늘려주면서 체크
-> 조건이 발생해서 귀찮아짐
1.2 섬 하나하나마다 간척사업 진행해서 최솟값 체크
-> 시간초과 발생할지 안할지 모르겠음

2. 한면 이상이 바다인 곳을 큐에 넣고 각각 bfs 돌리면서 섬 체크
근데 이렇게 하면 일단 섬을 grouping 해야함. 그래야 도착할 섬, 바다, 출발한 섬을 구분할 수 있다. 
-> 어짜피 시간초과임....
안됨

'''

from collections import deque
import sys
sys.setrecursionlimit(10**9)


dy = [-1,0,1,0]
dx = [0,1,0,-1]

def paint(MAP,y,x,idx): #Grouping
    queue = deque()
    queue.append([y,x])
    MAP[y][x] = idx
    visited = []

    while queue:
        y,x=queue.popleft()
        for dir in range(0,4):
            ny,nx=y+dy[dir],x+dx[dir]
            if 0<=ny<n and 0<=nx<n and [ny,nx] not in visited:
                if MAP[ny][nx] == 1:
                    MAP[ny][nx] = idx
                    visited.append([ny,nx])
                    queue.append([ny,nx])
    return MAP

def bfs(MAP,queue):
    oy,ox = queue[0]
    count = [[0 for _ in range(n)] for _ in range(n)]
    count[oy][ox] = 1
    visited = []
    idx = MAP[oy][ox]
    while queue:
        y,x=queue.popleft()
        for dir in range(0,4):
            ny,nx=y+dy[dir],x+dx[dir]
            if 0<=ny<n and 0<=nx<n and [ny,nx] not in visited:
                if MAP[ny][nx] not in [idx,0]:#바다도 아니고 자신의 섬도 아님
                    return count[y][x]
                if MAP[ny][nx] == 0:
                    visited.append([ny,nx])
                    count[ny][nx] = count[y][x]+1
                    queue.append([ny,nx])

if __name__ == "__main__":
    answer = 999999999
    n = int(sys.stdin.readline())
    MAP = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    idx = 2
    for y in range(0,n):
        for x in range(0,n):
            if MAP[y][x] == 1:
                MAP = paint(MAP,y,x,idx)
                idx += 1
                
    for group in range(2,idx):  
        LIST = deque()
        for y in range(0,n):
            for x in range(0,n):
                if MAP[y][x] == group: #타겟 섬이면서
                    LIST.append([y,x])
        answer = min(answer,bfs(MAP,LIST))
        
    print(answer)