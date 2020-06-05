#10026 적록색약 

import sys
from collections import deque
import copy
input=sys.stdin.readline
INF=sys.maxsize

dy=[-1,0,1,0]
dx=[0,1,0,-1]


def bfs(y,x,MAP,n,idx,color):
   queue=deque()
   queue.append((y,x))
   visited=[(y,x)]
   MAP[y][x]=idx
   while queue:
      y,x=queue.popleft()
      for dir in range(0,4):
         ny,nx=y+dy[dir],x+dx[dir]
         if n>ny>=0 and n>nx>=0 and MAP[ny][nx] in color:
            if (ny,nx) not in visited:
               visited.append((ny,nx))
               queue.append((ny,nx))
               MAP[ny][nx]=idx
   return MAP

if __name__ == "__main__":
   n=int(input())
   MAP=[list(input().rstrip()) for _ in range(n)]
   idx1,idx2=1,1
   MAP2=copy.deepcopy(MAP)
   for y in range(0,n):
      for x in range(0,n):
         if MAP[y][x]=='R':
            MAP=bfs(y,x,MAP,n,idx1,['R'])
            idx1+=1
         elif MAP[y][x]=='G':
            MAP=bfs(y,x,MAP,n,idx1,['G'])
            idx1+=1
         elif MAP[y][x]=='B':
            MAP=bfs(y,x,MAP,n,idx1,['B'])
            idx1+=1

   for y in range(0,n):
      for x in range(0,n):
         if MAP2[y][x] in ['R','G'] :
            MAP2=bfs(y,x,MAP2,n,idx2,['R','G'])
            idx2+=1
         elif MAP2[y][x]=='B':
            MAP2=bfs(y,x,MAP2,n,idx2,['B'])
            idx2+=1
   print(idx1-1,idx2-1)
