#1915 가장 큰 정사각형
'''
ㅋㅋㅋㅋㅋㅋㅋㅋ
넘 어렵다
역시 디피
'''
import copy
import sys
input=sys.stdin.readline

if __name__ =="__main__":
   n,m=map(int,input().split())
   MAP=[[0 for _ in range(m+2)] for _ in range(n+2)]
   for i in range(1,n+1):
      arr=input()
      for j in range(1,m+1):
         MAP[i][j]=int(arr[j-1])
   
   answer=0
   for y in range(1,n+1):
      for x in range(1,m+1):
         if MAP[y][x]!=0:
            MAP[y][x]=min(MAP[y-1][x-1],MAP[y][x-1],MAP[y-1][x])+1
            answer=max(answer,MAP[y][x])
   print(answer**2)


'''
4 4
0100
0111
1111
0111
'''