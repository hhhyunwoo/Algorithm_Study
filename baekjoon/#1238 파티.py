#1238 파티
'''
플로이드 와샬 알고리즘 문제집에 분류되어 있길래 플로이드 와샬로 접근했다가 시간초과가 발생했다. 
n이 1000이라서 사실 O(n^3) 을 하게되면 파이썬에서는 시간초과가 발생한다.

그래서 다익스트라로 접근하였다.

다익스트라로 하더라도 
1,2,,,,N -> X 로 가는 최단 경로를 구하고

X-> 1,2,3,,,N 으로 가는 최단 경로를 다 구해야하기 때문에 

O(N* 다익스트라 시간복잡도) 만큼 걸려서 될까 잠깐 고민했지만, 괜찮을 것 같았고 실제로 돌아갔다.

최단경로를 찾는 다익스트라 알고리즘을 적용해서 
1,2,,,,N -> X 

X-> 1,2,3,,,N 
를 구한 후 더해서 최대값을 출력하면 된다.
'''
import sys
import copy
import heapq
from collections import deque
input=sys.stdin.readline
inf=2**32

def bfs(start,end): 
   heap=[]
   heapq.heappush(heap,[dist[start],start])
   while heap:
      weight,cur=heapq.heappop(heap)
      if cur==end:return weight
      for to,cost in arr[cur]:
         if dist[to]>dist[cur]+cost:
            dist[to]=dist[cur]+cost
            heapq.heappush(heap,[dist[to],to])
   return inf


n,m,x=map(int,input().split())
arr={i:[] for i in range(1,n+1)}

for _ in range(m):
   a,b,c=map(int,input().split())
   arr[a].append([b,c])
   
res =[]
for start in range(1,n+1):
   #start~ x
   dist=[inf]*(n+1)
   dist[start]=0
   res.append(bfs(start,x))

for end in range(1,n+1):
   #x ~ end
   dist=[inf]*(n+1)
   dist[x]=0
   res[end-1]+=bfs(x,end)

print(max(res))
