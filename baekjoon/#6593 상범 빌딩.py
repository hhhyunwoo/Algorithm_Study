#6593 상범 빌딩



import sys
from collections import deque
from heapq import heappop,heappush
input=sys.stdin.readline

INF=sys.maxsize

#동서남북상하
dz=[0,0,0,0,1,-1]
dy=[0,0,1,-1,0,0]
dx=[1,-1,0,0,0,0]

def bfs(start_z,start_y,start_x,end_z,end_y,end_x,MAP,l,r,c):
   heap=[]
   heappush(heap,(0,[start_z,start_y,start_x]))
   visited = [[[INF for _ in range(c)] for _ in range(r)] for _ in range(l)]
   visited[start_z][start_y][start_x]=0
   while heap:
      weight,pos=heappop(heap)
      z,y,x=pos[0],pos[1],pos[2]
      for dir in range(0,6):
         nz,ny,nx=z+dz[dir],y+dy[dir],x+dx[dir]
         if l>nz>=0 and r>ny>=0 and c>nx>=0 and MAP[nz][ny][nx]!='#':
            if visited[nz][ny][nx]>weight+1:
               visited[nz][ny][nx]=weight+1
               heappush(heap,(visited[nz][ny][nx],[nz,ny,nx]))

   return visited[end_z][end_y][end_x]

if __name__ == "__main__":
   while 1:
      l,r,c = map(int,input().split())
      if l==r==c==0: break
      MAP=[]
      start_z,start_y,start_x,flag=0,0,0,0
      end_z,end_y,end_x=0,0,0
      for i in range(0,l):
         level = [list(str(input().rstrip())) for _ in range(r)]
         if flag !=2:
            for j in range(0,r):
               for k in range(0,c):
                  if level[j][k]=='S':
                     start_z,start_y,start_x=i,j,k
                     flag+=1
                  elif level[j][k]=='E':
                     end_z,end_y,end_x=i,j,k
                     flag+=1
         tmp=input()
         MAP.append(level)
      

      ans = bfs(start_z,start_y,start_x,end_z,end_y,end_x,MAP,l,r,c)
      if ans==INF:
         print("Trapped!") 
      else:
         print("Escaped in %d minute(s)." %ans)

