#5014 스타트링크

import sys
from collections import deque
input=sys.stdin.readline

def bfs():
   queue=deque()
   queue.append([s,0])
   visited=[0]*(f+1)
   visited[s]=1
   while queue:
      cur,cnt=queue.popleft()
      if cur==g:return cnt
      if cur+u<=f and visited[cur+u]==0:
         queue.append([cur+u,cnt+1])
         visited[cur+u]=1
      
      if 1<=cur-d and visited[cur-d]==0:
         queue.append([cur-d,cnt+1])
         visited[cur-d]=1
   return -1

f,s,g,u,d=map(int,input().split())
#총 f 층, s에서 시작, g로 가기, u,d
ans=bfs()
if ans==-1:print("use the stairs")
else:print(ans)