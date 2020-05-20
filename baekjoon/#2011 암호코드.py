#2011 암호코드
arr = '0'+str(input())
if arr[1] == '0':
    print('0')
else:
    dp=[0]*(len(arr)+1)
    dp[0],dp[1] = 1, 1
    for i in range(2,len(arr)):
        if int(arr[i])>0:
            dp[i] = dp[i-1]
        if 10<=int(arr[i-1:i+1])<=26:
            dp[i] += dp[i-2]
    print(dp[len(arr)-1]%1000000)