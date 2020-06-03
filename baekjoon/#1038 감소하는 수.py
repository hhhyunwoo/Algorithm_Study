#1038 감소하는 수

import sys
from collections import deque
from heapq import heappop,heappush
import copy
input=sys.stdin.readline

res=""
'''
1 3
-> 2자리수에 첫번째 수는 4
3 7
-> 4(row+1)자리수에 첫번째 수는 8
-> 8***
-> ***에 대해서 찾는데 ***은 3자리수에서 cnt2번째 수
그럼 row값이 (row-1)이고, cnt2번째 col를 찾아서 재귀돌리자
check(dp,row-1,cnt2)
여기서 col값과 cnt2를 찾는 함수를 만들어야함. 그게 find_big

엔드 조건은 row값이 0이면 즉, 한자리 수이면 cnt2-1값을 출력하면됨?
'''
def find_big(dp,row,order):
   tmp=0
   for i in range(0,9):
      tmp += dp[row][i]
      if tmp>=order:
         return i,order-(tmp-dp[row][i])

def check(dp,num,first,second): #dp,자리수,젤큰자리의 수, 몇번째인지
   global res
   if num==1:
      res+=str(first+1)+str(second-1)
      return
   else:
      res+=str(first+1)
      first,second=find_big(dp,num-1,second)
      check(dp,num-1,first,second)

if __name__ == "__main__":
   n=int(input())
   if n<=10:print(n)
   elif n>1022:
      print(-1)
   else:
      dp=[[0 for _ in range(10)] for _ in range(10)]
      for i in range(1,10):
         dp[0][i-1]=1
      dp[1][0]=1
      row=1
      cnt=10
      flag=0
      dp[0][9],dp[1][9]=9,1
      while flag!=1:
         SUM=0
         for col in range(1,10):
            if col==9: dp[row][col]+=SUM
            else:
               dp[row][col] = dp[row][col-1]+dp[row-1][col-1]
               SUM+=dp[row][col]
               cnt+=dp[row][col]
            if cnt>=n:
               cnt2=n-(cnt-dp[row][col])
               flag=1
               break
         row+=1

      #row + 1 자리수, col+1 젤 첫번째 수, cnt2번째 수
      check(dp,row-1,col,cnt2)

      print(res)
