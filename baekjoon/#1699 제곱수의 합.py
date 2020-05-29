#1699 제곱수의 합
n=int(input())
dp=[0,1]
for i in range(2,n+1):
   idx=1
   MIN=i
   while 1:
      if idx**2 <= i:
         MIN=min(MIN,dp[i-idx**2])
      else: break
      idx += 1
   dp.append(MIN+1)
print(dp[n])