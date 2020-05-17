#2775 부녀회장이 될테야

a = int(input())

for _ in range(a):
    k=int(input())
    n = int(input())
    dp = [[0 for _ in range(n)]for _ in range(k+1)]
    for i in range(0,n):
        dp[0][i] = i+1
    for i in range(1,k+1):
        dp[i][0] = 1
        for j in range(1,n):
            dp[i][j] = dp[i][j-1]+dp[i-1][j]
    print(dp[k][n-1])

