#1107 리모컨

from itertools import product

if __name__ == "__main__":
   num=int(input())
   m=int(input())
   if m!=0:
      arr=list(map(int,input().split()))
   else:
      arr=[]
   cur = 100
   answer=abs(num-cur)

   channel=[i for i in range(0,10) if i not in arr]
   for i in range(6,0,-1):
      for val in product(channel,repeat=i):
         tmp = ''.join(list(map(str,val)))
         tmp=int(tmp)
         length=len(str(tmp))
         if answer>(length+abs(num-tmp)):
            answer=(length+abs(num-tmp))

   print(answer)
