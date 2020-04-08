#10844
#2차원 리스트 선언하고싶을때 dp.append([])이렇게 할 수 있음
N = int(input())

dp = list()
dp.append([0,1,1,1,1,1,1,1,1,1])

for j in range(1,N):
    dp.append([])
    dp[j].append(dp[j-1][1])#0
    for i in range(1,9):
        value = dp[j-1][i-1] + dp[j-1][i+1]
        dp[j].append(value)
    
    dp[j].append(dp[j-1][8])#9
sum = 0
for k in range(0,10):
    sum += dp[N-1][k]

print(sum%1000000000)