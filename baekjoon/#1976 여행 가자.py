#1976 여행 가자

import sys
import math
from collections import deque
import copy
input=sys.stdin.readline
INF=sys.maxsize

def find(parent, n):
   tmp = n
   while 1:
      if parent[tmp]==tmp:
         return tmp
      tmp=parent[tmp]
   
if __name__ == "__main__":
   n=int(input())
   m=int(input())
   MAP=[list(map(int,input().split())) for _ in range(n)]
   val = list(map(int,input().split()))

   parent=[i for i in range(0,n+1)]
   for y in range(0,n):
      for x in range(y+1,n):
         if MAP[y][x]==1:
            parent[find(parent,x+1)]=find(parent,y+1)

   flag=0
   for i in range(0,m-1):
      start,end=val[i],val[i+1]
      if find(parent,start)!=find(parent,end):
         flag=1
         break

   if flag==1: print('NO')
   else: print('YES')
   
