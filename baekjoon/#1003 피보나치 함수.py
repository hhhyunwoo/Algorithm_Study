#1003 피보나치 함수

n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [[0,0] for _ in range(max(arr)+1)]
dp[0],dp[1] = [0,1],[1,0]

for i in range(2,max(arr)+1):
    dp[i][0] = dp[i-1][0]+dp[i-2][0]
    dp[i][1] = dp[i-1][1]+dp[i-2][1]

for a in arr:
    print(dp[a][1],dp[a][0])