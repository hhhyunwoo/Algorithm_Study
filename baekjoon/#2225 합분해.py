#2225 합분해

'''
dp라는 힌트 얻고 쉽게 풀었다!

단순히 몇개 진행해보면 2차원 dp로 쉽게 풀이 가능한 문제

 K 1 2 3 4 ... k
N  1 2 3 4 
1  1 3 6 10
2  1 4 10 
3
...
n
dp[row][col]=dp[row][col-1]+dp[row-1][col] 
라는 점화식이 나오며 풀이 가능
'''

from itertools import product

if __name__ == "__main__":
   n,k=map(int,input().split())
   dp = [[0 for _ in range(k+1)]for _ in range(n+1)]
   for i in range(1,n+1):dp[i][1]=1
   for i in range(1,k+1):dp[1][i]=i

   for row in range(2,n+1):
      for col in range(2,k+1):
         dp[row][col]=dp[row][col-1]+dp[row-1][col]
   print(dp[n][k]%1000000000)
