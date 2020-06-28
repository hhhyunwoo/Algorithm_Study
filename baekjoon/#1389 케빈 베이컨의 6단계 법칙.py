#1389 케빈 베이컨의 6단계 법칙

import sys
import copy
from collections import deque
input=sys.stdin.readline
inf=sys.maxsize

n,m=map(int,input().split())
arr=[[inf for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
   a,b=map(int,input().split())
   arr[a][b]=1
   arr[b][a]=1
for i in range(1,n+1):arr[i][i]=0

for k in range(1,n+1):
   for i in range(1,n+1):
      for j in range(1,n+1):
         arr[i][j]=min(arr[i][j],arr[i][k]+arr[k][j])
ans=[]
for i in range(1,n+1):
   ans.append(sum(arr[i][1:]))
MIN=min(ans)
res=[]
for i in range(0,n):
   if ans[i]==MIN:res.append(i+1)
print(min(res))