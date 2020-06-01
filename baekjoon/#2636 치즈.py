#2636 치즈

'''
우왕,,

고전했던 부분이 내부 공기와 외부 공기를 구분하는 것이었다.

아이디어가 생각이 안났는데 제일 가장자리 부분은 치즈가 놓여질 수 없다는 말을 듣고 생각났다.

0,0으로부터 0인 부분을 다른 값으로 채워주면 구분이 가능하다!


하,., 그런데 간과한 점이 있다.
만약 내부 공기에 외부공기가 유입된다면 다시 aircheck을 해주어야하는데 이 부분을 while 안에서 시간이 지날때마다 모든 공기를 다시 bfs 하니깐 시간초과가 발생한다.

이 부분이 상당히 어려웠다. 
https://www.software.kr/download/?filePath=L7xCi_2FhV76fukwTQ5Ef3DoUmbR9UndWaKupGXqB5iRlQRuncnseSdG8NVUwWIlvGeAoho10r18rE_0AUcloX3JQvQ_3D_3D
창의적 알고리즘 (중급) 부분 치즈 부분의 힌트를 조금 얻어서 풀게되었다.

단순하게 반복적으로 air를 체크하는 것이 아닌, 공기로 바뀌는 치즈 부분을 list로 만들어서 이 부분만 다시 bfs를 수행했다.

이렇게 하니깐, 확실히 시간이 줄어들었다.
정답률 49프로가 믿기지 않는 문제이다. ㅎㅎ

BFS는 물론 DFS(BFS로도 이용가능) 을 아주 응용한 문제라서 쉽지 않았다.

'''

import sys
from collections import deque
import copy
input=sys.stdin.readline

dy=[-1,1,0,0]
dx=[0,0,-1,1]

def air_check(y,x,MAP,row,col):
   queue = deque()
   queue.append((y,x))
   while queue:
      y,x=queue.popleft()
      for dir in range(0,4):
         ny,nx=y+dy[dir],x+dx[dir]
         if 0<=ny<row and 0<=nx<col and MAP[ny][nx]==0:
            MAP[ny][nx]=-1
            queue.append((ny,nx))
   return MAP


def check(MAP,row,col):
   count=0
   tmp = copy.deepcopy(MAP)
   changes=[]
   for y in range(0,row):
      for x in range(0,col):
         if MAP[y][x]==1:
            flag = 0
            for dir in range(0,4):
               ny,nx=y+dy[dir],x+dx[dir]
               if 0<=ny<row and 0<=nx<col:
                  if MAP[ny][nx]==-1: #공기 접촉
                     flag=1
                     break
            if flag==1:
               tmp[y][x]=-1 
               #치즈가 변경되는 부분으로 부터 aircheck를 해야하기떄문에 list를 만들어준다.
               changes.append([y,x])
               count+=1
   return tmp,count,changes

if __name__ == "__main__":
   row,col = map(int,input().split())
   MAP=[list(map(int,input().split())) for _ in range(row)]
   time,cnt2 = 0,0
   MAP = air_check(0,0,MAP,row,col) #맨첨에 바깥 공기를 구분한다.
   while 1:
      tmp,cnt,changes = check(MAP,row,col)
      if cnt==0:#치즈가 없다
         print(time)
         print(cnt2)
         break
      else:
         MAP=tmp

      for change in changes:
         MAP = air_check(change[0],change[1],MAP,row,col)
      time+=1
      cnt2=cnt