#1753 최단경로
from collections import deque
import heapq
import sys

INF = sys.maxsize
v,e=map(int,sys.stdin.readline().split())
k=int(sys.stdin.readline())
arr={i:[] for i in range(1,v+1)}
dist=[INF]*(v+1)
visited=[0]*(v+1)
dist[k]=0
#queue=deque()
#queue.append(k)
queue=[]
heapq.heappush(queue,(0,k))

for _ in range(e):
   u,v,w=map(int,sys.stdin.readline().split())
   arr[u].append([v,w])

while queue:
   weight, start = heapq.heappop(queue)
   #start=queue.popleft()
   if dist[start]<weight:continue
   
   #visited[start]=1
   for a in arr[start]:
      #if visited[a[0]]==0:
         #queue.append(a[0])
      if dist[a[0]] > dist[start]+a[1]:
         dist[a[0]] = dist[start]+a[1]
         heapq.heappush(queue,(dist[start]+a[1],a[0]))

for d in dist[1:]:
   if d==INF:print('INF')
   else:print(d)