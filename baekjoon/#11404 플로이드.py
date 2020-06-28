#11404 플로이드

import sys
import copy
from collections import deque
input=sys.stdin.readline
inf=2**32

n=int(input())
m=int(input())
arr=[[inf for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1):arr[i][i]=0
for _ in range(m):
   a,b,c=map(int,input().split())
   arr[a][b]=min(c,arr[a][b])
for k in range(1,n+1):
   for i in range(1,n+1):
      for j in range(1,n+1):
         arr[i][j]=min(arr[i][j],arr[i][k]+arr[k][j])
for i in range(1,n+1):
   for j in range(1,n+1):
      if arr[i][j]==inf:arr[i][j]=0
for i in range(1,n+1):
   print(*arr[i][1:])