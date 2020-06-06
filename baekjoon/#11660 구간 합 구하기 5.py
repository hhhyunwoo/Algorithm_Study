#11660 구간 합 구하기 5

import sys
from collections import deque
import copy
input=sys.stdin.readline
INF=sys.maxsize

if __name__ == "__main__":
   n,m=map(int,input().split())
   arr=[list(map(int,input().split())) for _ in range(n)]
   val=[list(map(int,input().split())) for _ in range(m)]
   dp=[[0 for _ in range(n+1)] for _ in range(n+1)]
   for y in range(1,n+1):
      for x in range(1,n+1):
         dp[y][x]=dp[y][x-1]+dp[y-1][x]-dp[y-1][x-1]+arr[y-1][x-1]
   
   for v in val:
      y1,x1,y2,x2=v[0],v[1],v[2],v[3]
      print(dp[y2][x2]-(dp[y2][x1-1]+dp[y1-1][x2]-dp[y1-1][x1-1]))
