#9205 맥주 마시면서 걸어가기
import sys
from collections import deque
input=sys.stdin.readline
t=int(input())
inf=2**32

def bfs(start):
    queue=deque([start])
    visited=[start]
    beer_dist=50*20
    while queue:
        cur=queue.popleft()
        if arr[cur][target] <= beer_dist:
            return 1
        for i in range(1,n+1):#모든 편의점을 본다
            if i not in visited and arr[cur][i]<=beer_dist:#방문 안한 편의점
                queue.append(i)
                visited.append(i)
    return -1

for _ in range(t):
    n=int(input())
    arr=[[inf for _ in range(n+2)] for _ in range(n+2)]
    #start_x,start_y=map(int,input().split())
    conv=[list(map(int,input().split())) for _ in range(n+2)]
    #end_x,end_y=map(int,input().split())
    for i in range(0,n+2):
        for j in range(0,n+2):
            arr[i][j]=abs(conv[i][0]-conv[j][0])+abs(conv[i][1]-conv[j][1])
    for k in range(0,n+2):
        for i in range(0,n+2):
            for j in range(0,n+2):
                arr[i][j]=min(arr[i][j],arr[i][k]+arr[k][j])
    home,target=0,n+1
    #50*20
    if bfs(home)==1:print("happy")
    else:print("sad")