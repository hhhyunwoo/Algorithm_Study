#1781 컵라면
import sys
import heapq 
from collections import deque
input=sys.stdin.readline

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
arr=sorted(arr,key=lambda k: k[0])
arr=deque(arr)
heap=[]
res=0
for time in range(n,0,-1):
    while arr and arr[-1][0]>=time:
        heapq.heappush(heap,-arr.pop()[1])
    if heap:
        res-=heapq.heappop(heap)
print(res)

'''
7
1 9
1 100
2 300
2 99
3 100
5 100
5 999
'''