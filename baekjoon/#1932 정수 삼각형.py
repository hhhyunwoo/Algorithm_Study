#1932 정수 삼각형
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    
    dp = [[0 for _ in range(n)]for _ in range(n)]
    dp[0][0] = arr[0][0]
    for i in range(1,n):
        for j in range(0,i+1):
            if j == 0: 
                dp[i][j] = arr[i][j]+ dp[i-1][j]
            elif j == i:
                dp[i][j] = arr[i][j]+ dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + arr[i][j]
    print(max(dp[n-1]))