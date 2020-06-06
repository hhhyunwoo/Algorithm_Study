#2042 구간 합 구하기
'''
세그먼트 트리

n개의 리프 노드
->
log(n)+1 의 높이
-> 
필요 노드 수 = 2^높이 -1

즉, 2^(log(n)+1)-1

https://blog.naver.com/ndb796/221282210534


진짜 개어렵다 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
예전에 알고리즘 수업시간에 HEAP 배우는 느낌...

'''
import sys
import math
from collections import deque
import copy
input=sys.stdin.readline
INF=sys.maxsize

def init(arr,tree,start,end,node):
   if start==end:
      tree[node]=arr[start]
   else:
      mid = (start+end)//2
      init(arr,tree,start,mid,node*2)
      init(arr,tree,mid+1,end,node*2+1)
      tree[node]=tree[node*2]+tree[node*2+1]

def update(tree,start,end,node,index,dif):
   if index<start or index>end: return
   #맨위에서 내려간다
   tree[node]+=dif
   if start==end:return
   mid = (start+end)//2
   update(tree,start,mid,node*2,index,dif)
   update(tree,mid+1,end,node*2+1,index,dif)

def sum(tree,start,end,node,left,right):
   if left>end or right<start:return 0
   if left<=start and end <=right: return tree[node]

   mid=(start+end)//2
   return sum(tree,start,mid,node*2,left,right)+sum(tree,mid+1,end,node*2+1,left,right)

if __name__ == "__main__":
   n,m,k=map(int,input().split())
   arr=[int(input()) for _ in range(n)]
   val=[list(map(int,input().split())) for _ in range(m+k)]
   tree_list=[0]*(pow(2,math.ceil(math.log(n,2))+1)-1)
   init(arr,tree_list,0,n-1,1)
   
   for v in val:
      b,c=v[1],v[2]
      if v[0]==1:
         update(tree_list,0,n-1,1,b-1,c-arr[b-1])
         arr[b-1]=c
      else:
         print(sum(tree_list,0,n-1,1,b-1,c-1))