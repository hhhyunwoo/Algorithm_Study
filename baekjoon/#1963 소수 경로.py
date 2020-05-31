#1963 소수 경로

import sys
from collections import deque
input=sys.stdin.readline

def make():
   check=[False,False]+[True]*9999
   prime=[]
   for i in range(2,10000):
      if check[i]:
         prime.append(i)
         idx=i*2
         while idx<10000:
            if check[idx]==True: 
               check[idx]=False
            idx +=i
   return prime

def bfs(start,end,prime):
   queue=deque()
   queue.append(start)
   visited= [start]
   check =[0 for _ in range(10001)]

   while queue:
      val = queue.popleft()
      if val==end:
         return check[val]
      for pos in range(0,4):
         for i in range(0,10):
            tmp = int(str(val)[:i] + str(i) + str(val)[i+1:])

            if tmp in prime:
               if tmp in visited:
                  if check[tmp]>check[val]+1:
                     check[tmp]=check[val]+1
                     queue.append(tmp)
                     visited.append(tmp)
               else:
                  check[tmp]=check[val]+1
                  queue.append(tmp)
                  visited.append(tmp)

if __name__ == "__main__":
   t=int(input())
   for _ in range(t):
      a,b=map(int,input().split())
      prime = make()
      print(bfs(a,b,prime))
