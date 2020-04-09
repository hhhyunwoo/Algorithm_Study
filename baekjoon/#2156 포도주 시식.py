#2156 포도주 시식
#개어려운데??
#ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 점화식 못세우게써우ㅜㅜ

'''현재를 기준으로
 X:O  이렇다면 arr[i] + dp[i-2]
XO:O     arr[i]+ arr[i-1] + dp[i-3] 왜냐면 어짜피 i-2도 x라서
  :X     dp[i-1]

https://limkydev.tistory.com/112

에서 아주 잘 설명해주셨다.
점화식 세우기 너무어렵다
진짜 토할 것 같다.
디피 너무어렵다.
'''



if __name__ == "__main__":
    N = int(input())
    arr = [0 for _ in range(10001)]
    dp = [0 for _ in range(10001)]

    for i in range(1,N+1):
        arr[i] = int(input())
    dp[1] = arr[1]
    if N > 1:
        dp[2] = arr[1]+arr[2]
        for k in range(3, N+1):
            a = arr[k] + arr[k-1] + dp[k-3]
            b = arr[k] + dp[k-2]
            c = dp[k-1]
            dp[k] = max(a,b,c)
    
    print(dp[N])