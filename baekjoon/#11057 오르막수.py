#11057 오르막수
N = int(input())

dp = [[0]*10 for _ in range(N+1)]

for i in range(0,10):
    dp[1][i] = 1

for i in range(2,N+1):
    for p in range(0,10):
        for k in range(p,10):
            dp[i][p] += dp[i-1][k]

sum = 0
for k in range(0,10):
    sum += dp[N][k]

print(sum%10007)

