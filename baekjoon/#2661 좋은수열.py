#2661 좋은수열

import sys
import re
input=sys.stdin.readline

ans=int('9'*81)
def dfs(val):
   global ans
   if len(val)==n:
      if ans>int(val):
         ans=int(val)
      return 0
   for i in range(1,4):
      tmp =val+str(i)
      flag=0
      for k in range(1,len(tmp)//2+1):
         if tmp[-k:]==tmp[-2*k:-k]:
            flag=1
            break
      if flag==1:
         continue
      else:
         if dfs(tmp)==0:return 0
n=int(input())
dfs('')
print(ans)