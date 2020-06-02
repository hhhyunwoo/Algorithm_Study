#1261 알고스팟

import sys
from collections import deque
from heapq import heappop,heappush
import copy
input=sys.stdin.readline

dy=[-1,1,0,0]
dx=[0,0,-1,1]

def bfs(MAP,row,col):
   heap= []
   heappush(heap,(0,0,0))
   visited=[[sys.maxsize for _ in range(col)]for _ in range(row)]
   visited[0][0]=0
   while heap:
      cnt,y,x=heappop(heap)
      for dir in range(0,4):
         ny,nx=y+dy[dir],x+dx[dir]
         if 0<=ny<row and 0<=nx<col:
            if MAP[ny][nx]=='1':
               if visited[ny][nx]>visited[y][x]+1:
                  visited[ny][nx]=visited[y][x]+1
                  heappush(heap,(cnt+1,ny,nx))
            else:
               if visited[ny][nx]>visited[y][x]:
                  visited[ny][nx]=visited[y][x]
                  heappush(heap,(cnt,ny,nx))
   return visited[row-1][col-1]

if __name__ == "__main__":
   col,row = map(int,input().split())
   MAP=[list(str(input().rstrip())) for _ in range(row)]
   ans = bfs(MAP,row,col)
   print(ans)

'''
3 5
001
101
001
011
000
'''