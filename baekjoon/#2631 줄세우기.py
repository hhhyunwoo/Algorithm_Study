#2631 줄세우기

'''
솔직히 첨에 어떻게 푸는지 감도 안왔다.

DP라는 힌트보고도 잘 모르겠더라.

그래서 조금 힌트를 얻어서 최장 길이 부분 수열 즉, LIS라는 힌트를 얻게되었다.

백준의 11053문제 (가장 긴 증가하는 부분 수열) 문제와 동일하다.
https://www.acmicpc.net/problem/11053



이참에 LIS 알고리즘을 한번 살펴보자
*LIS- Longest Increasing Subsequence

주어진 배열에서 가장 길게 증가하는 부분 수열을 찾아내는 알고리즘이다.
dp를 사용해서 메모이제이션 기법을 이용한다.

2포인터를 사용하는데 현재의 위치와 이전 위치의 값들을 비교해준다.
왼쪽에서 오른쪽으로 한칸씩 이동하는데 dp에 담긴 값의 의미는 현재 값까지 최장 길이 부분 수열은 무엇인가 이다.

예를 들어
3 7 5 2 6 1 4
에서 dp는
1 2 2 1 3 1 4가 된다.

왜냐하면
먼저 dp[0]은 1로 초기화 해주고

for i in range(1,n):
      for j in range(0,i):
         if arr[i] > arr[j]:
이렇게 i는 현재값, 그리고 비교 하는 부분은 이전의 값들 j = 0~i-1 이다.
만약 j의 값이 i의 값보다 작다면 증가하는 부분수열이 가능하다.
그렇다면 j 의 dp 값에 1칸 더한 것 만큼 길이가 가능하다는 의미이다.

따라서 가능한 j의 dp의 최대값을 구한 후 그 값에 1을 더해서 dp[i]에 대입한다.

이렇게 끝까지 가면 최대값을 찾을 수 있다.




줄세우기 문제에서 이렇게 구한 dp값의 최대값의 의미는 최대값 만큼은 움직일 필요가 없다는 의미이다.
따라서 n - 최대값을 하게 되면 정답을 알 수 있다.
'''


import sys
from collections import deque
input=sys.stdin.readline


if __name__ == "__main__":
   n=int(input())
   arr=[int(input()) for _ in range(n)]
   dp=[0 for _ in range(n)]
   dp[0]=1
   MAX=0
   for i in range(1,n):
      for j in range(0,i):
         if arr[i] > arr[j]:
            MAX = max(MAX,dp[j])
      dp[i]=MAX+1
      MAX=0
   print(n-max(dp)) 