#10775 공항

import sys
import math
from collections import deque
import copy
input=sys.stdin.readline
INF=sys.maxsiz
      #collapsing process
      #이 과정 없이 단순하게 while이나 재귀로 find하면 노드끼리의 길이가 무한정 길어지기 때문에 collapsing으로 트리의 높이를 낮춘다.
      
def find(parent, n):
   if n==parent[n]: return n
   else:
      parent[n] = find(parent,parent[n])
      return parent[n]
      
def union(parent,x,y):
   x,y=find(parent,x),find(parent,y)
   parent[x]=y
   
if __name__ == "__main__":
   g=int(input())
   p=int(input())
   arr=[int(input()) for _ in range(p)]
   parent=[i for i in range(0,g+1)]

   cnt=0
   for i in range(0,p):
      tmp=find(parent,arr[i]) 
      if tmp== 0:
         break
      else:
         union(parent,tmp,tmp-1)
         cnt+=1
   print(cnt)
