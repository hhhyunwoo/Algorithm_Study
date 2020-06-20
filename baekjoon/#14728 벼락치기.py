#14728 벼락치기
import sys
from collections import deque
input=sys.stdin.readline

n,t=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
'''
dp=[[0 for _ in range(t+1)] for _ in range(n+1)]

for num in range(1,n+1):
   for time in range(1,t+1):
      if arr[num-1][0]>time:
         dp[num][time]=dp[num-1][time]
      else:
         dp[num][time] = max(dp[num-1][time], dp[num-1][time-arr[num-1][0]]+arr[num-1][1])
print(dp[n][t])

'''
dp = [0]*(t+1)

for Time,Score in arr:
   for j in range(t,Time-1,-1):
      dp[j]=max(dp[j], dp[j-Time]+Score)
print(dp[t])
