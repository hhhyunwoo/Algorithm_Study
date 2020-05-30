#1913 달팽이

n=int(input())
m=int(input())
arr=[[0 for _ in range(n)] for _ in range(n)]

for i in range(0,n//2+1):
   arr[i][i] = (n-(2*i))**2
   val=(n-(2*(i+1)))**2 +1
   y,x=i,i
   dir = 0
   while 1:
      if y==i and x==i and dir==3:
         if i==n//2:
            arr[y][x]=1
         break
      if dir == 0:#우측
         x+=1
      elif dir==1:#하
         y+=1
      elif dir==2:#좌
         x-=1
      elif dir == 3:#상
         y-=1
      if x<i :
         x+=1
         dir=3
         continue
      elif x>=(n-i):
         x-=1
         dir=1
         continue
      elif y>=(n-i):
         y-=1
         dir=2
         continue

      arr[y][x] = val
      val+=1

for i in range(0,len(arr)):
   if m in arr[i]:
      res = [i+1,arr[i].index(m)+1]
   print(*arr[i])
print(*res)