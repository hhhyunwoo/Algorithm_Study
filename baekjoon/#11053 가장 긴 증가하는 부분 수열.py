#11053 가장 긴 증가하는 부분 수열
#걍 너무 어렵다 dp는
'''
이 문제는 현재 값을 찾기 위해 이전 배열을 다 둘러봐야한다. 
https://wootool.tistory.com/96
이 블로그에서 그림을 포스팅해뒀는데 아주 이해가 잘된다.

즉, 현재 값의 길이를 생각하려면 이전 값들을 둘러보면서 만약 자신보다 작다면 그 값의 최대길이에다가 1을 더해주면된다. 근데 자신보다 작은 값이 여러개 있을 것이다. 그들 중 max값을 가지고 +1 해주면 된다. 
'''

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int,input().split()))
    dp = [0 for _ in range(1001)]
    MAX = 0
    dp[0] = 1

    for i in range(1,N):
        for j in range(0,i):
            if arr[j] < arr[i]:
                MAX = max(MAX,dp[j])
        dp[i] = MAX + 1
        MAX = 0
    print(max(dp))

