#11403 경로 찾기

import sys
import copy
from collections import deque
input=sys.stdin.readline
inf=sys.maxsize

n=int(input())
MAP = [list(map(int,input().split())) for _ in range(n)]
arr=[[inf for _ in range(n)] for _ in range(n)]
#for i in range(0,n):arr[i][i]=0
for i in range(0,n):
   for j in range(0,n):
      if MAP[i][j]==1: arr[i][j]=1

for k in range(0,n):
   for i in range(0,n):
      for j in range(0,n):
         arr[i][j]=min(arr[i][j],arr[i][k]+arr[k][j])

for i in range(0,n):
   res=[]
   for j in range(0,n):
      if arr[i][j] not in [inf,0]:
         res.append(1)
      else:res.append(0)
   print(*res)