#1697 숨바꼭질

from collections import deque
def bfs(n,k):
   queue = deque()
   queue.append(n)
   check=[99999]*100001
   visited=[0]*100001
   visited[n],check[n]=1,0
   while queue:
      pos = queue.popleft()
      if pos == k:
         return check[k]
      if pos*2 < 100001 and visited[pos*2]==0:
         visited[pos*2]=1
         queue.append(pos*2)
         check[pos*2] = check[pos]+1
      if pos-1 >= 0 and visited[pos-1]==0:
         visited[pos-1]=1
         queue.append(pos-1)
         check[pos-1] = check[pos]+1
      if pos+1 < 100001 and visited[pos+1]==0:
         visited[pos+1]=1
         queue.append(pos+1)
         check[pos+1] = check[pos]+1
      
if __name__ == "__main__":
   n,k=map(int,input().split())
   print(bfs(n,k))