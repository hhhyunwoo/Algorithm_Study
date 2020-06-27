#2606 바이러스

import sys
import copy
from collections import deque
input=sys.stdin.readline
inf=sys.maxsize

n=int(input())
k=int(input())
for i in range(1,n+1): arr[i][i]=0
edge={i:[] for i in range(1,n+1)}
for _ in range(k):
   a,b=map(int,input().split())
   edge[a].append(b)
   edge[b].append(a)

res,queue,visited=[],[1],[1]
while queue:
   cur=queue.pop(0)
   for i in edge[cur]:
      if i not in visited:
         queue.append(i)
         visited.append(i)
         res.append(i)

print(len(res))