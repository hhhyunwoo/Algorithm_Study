#4869 종이붙이기


T = int(input())

for TC in range(1, T + 1):
    N = int(input())
    dp = list()
    dp.append(1)
    dp.append(3)
    for i in range(2,N//10):
        num = dp[i-1] + dp[i-2] * 2
        dp.append(num)

    print("#%d %d" %(TC, dp[i]))