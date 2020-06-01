#2589 보물섬
import sys
from collections import deque
input=sys.stdin.readline

dy=[-1,1,0,0]
dx=[0,0,-1,1]
def bfs(y,x,MAP,row,col):
    queue=deque()
    queue.append((y,x))
    res=0
    check=[[0 for _ in range(col)] for _ in range(row)]
    check[y][x]=1
    while queue:
        y,x=queue.popleft()
        for dir in range(0,4):
            ny,nx=y+dy[dir],x+dx[dir]
            if row>ny>=0 and col>nx>=0 and [ny,nx] and check[ny][nx]==0:
                if MAP[ny][nx]=='L':
                    queue.append((ny,nx))
                    check[ny][nx]=check[y][x]+1
                    res=max(res,check[ny][nx])
    return res-1


if __name__ == "__main__":
    row,col=map(int,input().split()) #세로 가로
    MAP=[list(input().rstrip()) for _ in range(row)]
    ans=0
    for y in range(0,row):
        for x in range(0,col):
            if MAP[y][x] == 'L':
                ans = max(ans,bfs(y,x,MAP,row,col))
    print(ans)