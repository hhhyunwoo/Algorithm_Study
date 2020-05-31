#1916 최소비용 구하기

'''
heap을 통해서 갈수 있는 경로 중 가장 짧은 경로를 pop해준다. 그래서 안에 값에 weight와 위치를 같이 넣는다.

아 visited가 필요없는 이유 ! 
-> 단방향이기 때문에 다시 돌아갈 일이 없다. 만약 visited로 막아버리면 
예를들어
1->4는 한번 탐색했지만 1->2->4 가 더 짧은 경우일 수도 있기때문에 모든 경우를 탐색해봐야한다. 따라서 visited로 막으면 안된다.


흠,,, 문제 좀 오바인듯?? 버스가 여러대 있을 수 있다는 조건을 적어줘야 체크를하지,,,
'''


import sys
from heapq import heappop,heappush 
input=sys.stdin.readline
INF=sys.maxsize

def dijk(MAP,start):
   dist=[INF for _ in range(n+1)]
   dist[start]=0
   heap=[]
   heappush(heap,(0,start))

   while heap:
      weight,cur=heappop(heap)
      for v in range(1,n+1):
         if MAP[cur][v]!=-1:
            if dist[v] > MAP[cur][v] + weight:
               dist[v] = MAP[cur][v] + weight
               heappush(heap,(dist[v],v))
   return dist


if __name__ == "__main__":
   n,m=int(input()),int(input())
   MAP=[[-1 for _ in range(n+1)] for _ in range(n+1)]
   for _ in range(m):
      u,v,w=map(int,input().split())
      if MAP[u][v] != -1: #같은버스 여러대?
         MAP[u][v]=min(MAP[u][v],w)
      else: MAP[u][v]=w
   start,end=map(int,input().split())
   answer = dijk(MAP,start)
   #print(answer)
   print(answer[end])
