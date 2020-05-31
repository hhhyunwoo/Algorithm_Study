#2493 탑

'''
흠, 생각하는게 쉬운가??
스택이라는 힌트 얻고도 꽤 고민했다.
입력값을 하나씩 받으면서 스택을 이용한다.

키포인트는 만약 스택에 있는 값을 top에서 부터 보는데 들어온 입력값보다 스택의 값이 작다면 pop해준다.
pop해주는 것이 나중에 뒤의 값에 영향을 미치지 않는 이유는 현재의 값이 더 크기 때문에 어짜피 현재 값에서 걸릴 것이기 때문이다!!

그래서 pop해주면서 stack 이 비거나, 자신보다 크거나 같은 값이 들어올때까지 돌아준다.

그렇게 풀어주면 쉽게 해결 가능하지만 이런 기법자체를 생각한다는게 쉽지만은 않은듯,,,
'''

import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
stack=[]
ans=[]
for i in range(0,n):
   while 1:
      if not stack:
         stack.append((i,arr[i]))
         ans.append(0)
         break
      if stack[-1][1]>=arr[i]:
         ans.append(stack[-1][0]+1)
         stack.append((i,arr[i]))
         break
      else:
         stack.pop()
print(*ans)