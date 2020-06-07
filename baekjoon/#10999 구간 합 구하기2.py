#10999 구간 합 구하기2
'''
https://www.acmicpc.net/blog/view/26

https://www.acmicpc.net/source/20153968

진짜 너무너무 어렵당...

일반 세그먼트 트리도 어려운데 구간 update 즉, Lazy Propagation 알고리즘까지 적용하려니깐 진짜 어렵다.

'''
import sys
import math
from collections import deque
import copy
input=sys.stdin.readline
INF=sys.maxsize


#맨처음에 tree 초기화.
#start,end는 data의 index이다. 
#node는 최상위 노드 1부터 쭉 이어짐.
def init(arr,tree,start,end,node):
   #leaf노드라는 의미
   #즉, start~end 가 구간의 의미인데 같다는 것은 하나의 노드만을 가르킨다는 의미
   #리프노드일때는 그 index의 값을 해당 노드에 저장한다.
   if start==end:
      tree[node]=arr[start]
      
   #리프노드가 아니라 구간일때는 재귀함수를 통해서 mid를 기준으로 수행
   else:
      mid = (start+end)//2
      init(arr,tree,start,mid,node*2)
      init(arr,tree,mid+1,end,node*2+1)
      #재귀가 끝나고 해당 노드에서는 자식 노드 둘의 합을 저장함.
      tree[node]=tree[node*2]+tree[node*2+1]


def update_lazy(tree,lazy,node,start,end):
   #만약 해당 노드의 lazy 값이 존재한다면
   if lazy[node] !=0:
      # 해당 노드의 값을 update해준다.
      tree[node] += (end-start+1)*lazy[node]
      # 리프노드가 아니라면 lazy 값을 자기의 자식 값으로 내려준다.
      if start!=end:
         lazy[node*2]+=lazy[node]
         lazy[node*2+1]+=lazy[node]
      #그리고 자신의 lazy는 초기화
      lazy[node]=0


#일반 update가 아니라 구간의 update를 수행함
#Lazy Propagation 알고리즘을 통해서 구간의 업데이트 에서는 꼭 필요할 때가 오기 전까지는 업데이트를 수행하지 않음.
#쉽게 말해서 해당 노드가 우리가 update하고 싶은 구간을 모두 포함하고 있다면 lazy Propagation을 수행하고, 
# 그게아니라 해당 노드가 update하고 싶은 구간의 일부 부분만을 포함하고 있다면 일반적인 update_range 코드가 수행된다.
def update_range(tree,lazy,start,end,node,idx_start,idx_end,dif):
   update_lazy(tree,lazy,node,start,end)
   #update range가 해당 노드의 구간에 벗어나면 의미없음->리턴
   if idx_start>end or idx_end<start: return

   # 만약 update range가 해당노드의 모든 곳을 포함하고 있다면
   # lazy 값을 update해준다.
   if idx_start<=start and end<=idx_end:
      tree[node]+=(end-start+1)*dif
      if start!=end:
         lazy[node*2]+=dif
         lazy[node*2+1]+=dif
      return

   # 일부만 포함한다면 재귀함수를 통해서 다시 update_range를 수행한다.
   mid = (start+end)//2
   update_range(tree,lazy,start,mid,node*2,idx_start,idx_end,dif)
   update_range(tree,lazy,mid+1,end,node*2+1,idx_start,idx_end,dif)
   tree[node]=tree[node*2]+tree[node*2+1]


#구간합을 구하는 함수
#Lazy Propagation 을 쓸 때 조심해야하는 부분은 lazy 값을 SUM에서 처리해주어야 한다는 것이다.
#즉 나중에 업데이트한다는 의미가 sum을 구할때 lazy를 적용해준다는 의미이다.
def sum(tree,lazy,start,end,node,left,right):
   update_lazy(tree,lazy,node,start,end)
   #만약 구하고 싶은 구간이 start~end에 벗어난다면 0을 리턴
   if left>end or right<start:return 0
   # start~end에 구하고 싶은 구간이 전부 포함된다면 해당 노드의 값을 리턴
   if left<=start and end <=right: return tree[node]

   # 그게아니라면 재귀함수로 다시 파고 들어간다.
   mid=(start+end)//2
   return sum(tree,lazy,start,mid,node*2,left,right)+sum(tree,lazy,mid+1,end,node*2+1,left,right)

if __name__ == "__main__":
   n,m,k=map(int,input().split())
   arr=[int(input()) for _ in range(n)]
   val=[list(map(int,input().split())) for _ in range(m+k)]
   
   #트리 구성은 단순하게 *4로하면 넉넉하게 가능
   #완전하게 하고 싶다면 아래의 식을 대입하여 높이를 구하고 수행 가능
   #tree_list=[0]*(pow(2,math.ceil(math.log(n,2))+1)-1)
   tree_list=[0]*(n*4)
   lazy=[0]*(n*4)
   init(arr,tree_list,0,n-1,1)
   
   for v in val:
      b,c=v[1],v[2]
      if v[0]==1: #b~c까지 d를 더함
         d=v[3]
         update_range(tree_list,lazy,0,n-1,1,b-1,c-1,d)
      else:
         print(sum(tree_list,lazy,0,n-1,1,b-1,c-1))