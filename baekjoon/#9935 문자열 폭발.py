#9935 문자열 폭발
#https://ksshlee.github.io/baekjoon/%EB%B0%B1%EC%A4%80-9935-%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%8F%AD%EB%B0%9C/

'''
stack 두개를 이용해서 풀어봤는데 계속 시간초과가 발생했다 ㅜㅜ
'''

import sys
import re
input=sys.stdin.readline

arr=list(input().rstrip())
val=list(input().rstrip())
len_val=len(val)
stk=[] 
i=0
while i<len(arr):
   stk.append(arr[i])
   if len(stk)>= len_val:#문자열이 폭탄보다 커지면 검사
      s,e,flag=len(stk)-1,len(val)-1,0
      for _ in range(len_val):
         if stk[s] !=val[e]: 
            flag=1 
            break
         s-=1 
         e-=1
      if flag==0:
         for _ in range(len_val): stk.pop()
   i+=1
if not stk:print("FRULA")
else:print(''.join(stk))