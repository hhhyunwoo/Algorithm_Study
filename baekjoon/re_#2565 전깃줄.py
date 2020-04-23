re_#2565 전깃줄

'''
dfs 로 접근했는데 바로 시간초과,,,

좀 찾아봤더니 LIS 알고리즘을 사용해야한다고 한다.

보통 어떤 것을 제거해야하는지를 접근하지만, 이번 경우는 어떤 것을 추가할 것인가라는 방법으로 접근을 해야한다.
'''
import sys

answer = 999999999

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    MAP = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    MAP = sorted(MAP,key=lambda k: k[0])
    
    dp = [0] * (N+1)

    for i in range(0,len(MAP)):
        dp[i] = 1
        for j in range(0,i):
            if MAP[i][1] > MAP[j][1]:
                if dp[j]>= dp[i]:
                    dp[i] = dp[j] + 1
    
    print(N-max(dp))