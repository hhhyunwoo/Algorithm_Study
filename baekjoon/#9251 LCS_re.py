#9251 LCS 

'''
맨첨에 lis 알고리즘 푸는 방법으로 접근했다.
테스트 케이스는 다 맞았는데 
예를들어
ABCD
DBCA
같은 경우는 A가 젤 끝 A와 다시 비교되어서 B를 다시 보지 못한다.

따라서 dp가 1차원이 아닌 2차원이 되어야한다.
그래서 새로운 알고리즘으로 다시 접근해야했다.

'''

import sys
from collections import deque
import copy
input=sys.stdin.readline
INF=sys.maxsize

if __name__ == "__main__":
   arr1=list(input().rstrip())
   arr2=list(input().rstrip())
   dp=[[0 for _ in range(len(arr1)+1)] for _ in range(len(arr2)+1)]
      for y in range(1,len(arr2)+1):
         for x in range(1,len(arr1)+1):
            if arr2[y-1]==arr1[x-1]:
               dp[y][x]=dp[y-1][x-1]+1
            else:
               dp[y][x]=max(dp[y-1][x],dp[y][x-1])
   print(dp[-1][-1])
