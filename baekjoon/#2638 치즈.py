#2638 치즈

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
                     flag+=1
            if flag>=2:
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
         break
      else:
         MAP=tmp

      for change in changes:
         MAP = air_check(change[0],change[1],MAP,row,col)
      time+=1
      cnt2=cnt