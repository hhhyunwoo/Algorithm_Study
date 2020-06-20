#12865 평범한 배낭
import sys
from collections import deque
input=sys.stdin.readline

n,k=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
'''dp=[[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1,n+1):
   for w in range(1,k+1):
      if arr[i-1][0] > w: #넣고싶은 물건의 무게가 가방 크기보다 더 크다
         dp[i][w]=dp[i-1][w]
      else:#그전 물건을 넣기 전의 가치에다가 지금 물건을 넣은 가치 vs 지금것 안넣고 이전까지의 최댓값
         dp[i][w]=max(dp[i-1][w-arr[i-1][0]]+arr[i-1][1],dp[i-1][w]) 
'''
dp=[0 for _ in range(k+1)]
for W,V in arr:
   for j in range(k,W-1,-1):
      dp[j]=max(dp[j],dp[j-W]+V)

print(dp[k])