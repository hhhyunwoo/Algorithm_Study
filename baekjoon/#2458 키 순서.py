#2458 키 순서
import sys
from collections import deque
input=sys.stdin.readline
inf = 2*32

n,m=map(int,input().split())
arr=[[inf for _ in range(n+2)] for _ in range(n+2)]
for _ in range(m):
    a,b=map(int,input().split())
    arr[a][b]=1
for i in range(1,n+1):arr[i][i]=0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            arr[i][j]=min(arr[i][j],arr[i][k]+arr[k][j])
res=[]
for i in range(1,n+1):
    tmp=[]
    for j in range(1,n+1):
        if arr[i][j]==inf: #못간다는 의미
            tmp.append(j)
    flag=0
    for t in tmp:
        if arr[t][i]==inf:
            flag=1
            break
    if flag==0:
        res.append(i)
print(len(res))