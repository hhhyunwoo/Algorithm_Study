#2667 단지번호붙이기

#MAP에서 BFS를 사용하는 간단한 문제!

import sys
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(y,x):
    queue = list()
    queue.append((y,x))
    cnt = 1
    MAP[y][x] =-1
    while queue:
        pos = queue.pop(0)
        y = pos[0]
        x = pos[1]
        for dir in range(0,4):
            newy = y +dy[dir]
            newx = x +dx[dir]
            if 0<=newy<N and 0<=newx<N and MAP[newy][newx] == 1:
                MAP[newy][newx] =-1
                cnt += 1
                queue.append((newy,newx))
    return cnt

if __name__ == "__main__":
    N = int(input())
    MAP = [[0 for _ in range(N)] for _ in range(N)]
    arr = [str(input()) for _ in range(N)]
    for i in range(0,N):
        for j in range(0,N):
            MAP[i][j] = int(arr[i][j])
    ans = list()
    for j in range(0,N):
        for i in range(0,N):
            if MAP[j][i] == 1:
                ans.append(bfs(j,i))
    ans = sorted(ans)
    print(len(ans))
    for i in range(0,len(ans)):
        print(ans[i])