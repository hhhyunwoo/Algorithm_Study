#16234 삼성기출 인구 이동

#결국 시간초과,,, 흠, 잘 모르겠다 어디가 문제인지


import sys
import copy
from collections import deque

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(y,x,visited,idx):
    queue = deque()
    queue.append((y,x))
    visited[y][x] = idx
    count = 1

    size = 1
    people = MAP[y][x]

    while queue:
        pos = queue.popleft()
        y = pos[0]
        x = pos[1]
        for dir in range(0,4):
            newy = y+ dy[dir]
            newx = x+ dx[dir]
            if 0<=newy<N and 0<=newx<N and visited[newy][newx] == 0:
                if L <= abs(MAP[newy][newx] - MAP[y][x]) <= R:
                    visited[newy][newx] = idx
                    queue.append((newy,newx))
                    count += 1
                    size += 1
                    people += MAP[newy][newx]
                    
    return (count,people//size)


def migrate(p,idx):
    for y in range(0,N):
        for x in range(0,N):
            if visited[y][x] == idx:
                MAP[y][x] = p

if __name__ == "__main__":
    N,L,R = map(int,sys.stdin.readline().split())
    MAP = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    idx = 1
    cnt = 0

    while 1:
        visited = [[0 for _ in range(N)]for _ in range(N)]
        idx = 1
        flag = 0
        for j in range(0,N):
            for i in range(0,N):
                if visited[j][i] == 0: #연합이 이루어지지 않은 나라가 있으면 
                    temp = bfs(j,i,visited,idx)
                    if temp[0] > 1: #cnt > 1 이어야 인구이동
                        migrate(temp[1],idx)
                        flag = 1
                    idx += 1

        if flag == 0:
            print(cnt)
            break
                        
        cnt += 1 #인구이동 횟수