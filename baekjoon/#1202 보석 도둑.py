#1202 보석 도둑
import sys
import heapq
from collections import deque
input=sys.stdin.readline

n,k=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
arr=deque(sorted(arr,key=lambda k: k[0]))
bags=[int(input()) for _ in range(k)]
bags=sorted(bags)
heap=[]
res=0

for bag in bags:
    capacity=bag
    while arr and arr[0][0]<=capacity:
        heapq.heappush(heap,-arr.popleft()[1])
    if heap:res-=heapq.heappop(heap)
print(res)