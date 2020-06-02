#3055 탈출

import sys
from collections import deque
import copy
input=sys.stdin.readline

dy=[-1,1,0,0]
dx=[0,0,-1,1]

def bfs(end_y,end_x,start_y,start_x,MAP,row,col):
   queue,next_q = deque(),deque()
   queue.append((start_y,start_x))
   visited=[[0 for _ in range(col)]for _ in range(row)]
   visited[start_y][start_x]=1
   time=0
   while 1:
      tmp=copy.deepcopy(MAP) #물이 넘치는 부분
      for y in range(0,row):
         for x in range(0,col):
            if MAP[y][x]=='*':
               for dir in range(0,4):
                  ny,nx=y+dy[dir],x+dx[dir]
                  #물은 비어있는 곳만 찬다.
                  if 0<=ny<row and 0<=nx<col and MAP[ny][nx]=='.':
                     tmp[ny][nx]='*'
      MAP=tmp
      if not queue: return 'KAKTUS'

      while queue:
         y,x=queue.popleft()
         if (y,x) == (end_y,end_x):return time
         for dir in range(0,4):
            ny,nx=y+dy[dir],x+dx[dir]
            #고슴도치는 물, 돌 통과 X
            if 0<=ny<row and 0<=nx<col and visited[ny][nx]==0 and MAP[ny][nx]!='*' and MAP[ny][nx]!='X':
               visited[ny][nx]=1
               next_q.append((ny,nx))
      queue.extend(next_q)
      next_q=[]
      time+=1

if __name__ == "__main__":
   row,col = map(int,input().split())
   MAP=[list(str(input().rstrip())) for _ in range(row)]
   for y in range(0,row):
      for x in range(0,col):
         if MAP[y][x] == 'S':
            start_y,start_x=y,x
         elif MAP[y][x] == 'D':
            end_y,end_x=y,x
   ans = bfs(end_y,end_x,start_y,start_x,MAP,row,col)
   print(ans)