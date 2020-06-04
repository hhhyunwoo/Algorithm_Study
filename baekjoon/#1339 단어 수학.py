#1339 단어 수학

'''
맨첨에 permutation으로 싹 다 돌려서 max 값을 계산했다.
근데 알파벳의 개수가 10개일때는 몇개야,,, 10^10 인가 10!인가...
어쨌든 시간초과 발생!!

살짝 그리디 적인 방법으로 풀어야한다.
확실히 골드4넘어오니깐 문제들이 넘 어렵다...


자리수를 기준으로 가중치를 부여한다.
만약 중복되는 수가 있더라도 상관없다.
왜냐면 어짜피 더해주는 값이기 때문에 저게되든 이게되든 더한 값은 동일하다!

라고 생각을 했으나,,,,,
ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

내가 코드를 잘 못 짰었다...
10의 제곱수 값을 그냥 대입하는 것이 아니라 각 값에 더해주어야 한다.

만약 입력 값이

ABC
ACB
CAA
일때

A: 100 + 100 + 10 + 1
B: 10 + 1
C: 1 + 10 + 100
이렇게 해주어야 올바른 가중치 값이 나온다.
'''

import sys
import operator
input=sys.stdin.readline

if __name__ == "__main__":
   n=int(input())
   arr=[list(input().rstrip()) for _ in range(n)]
   alp=[]
   for a in arr:
      for b in a:
         alp.append(b)
   alp=list(set(alp))
   alp={i:0 for i in alp}
   res={i:0 for i in alp}
   for a in arr:
      j=1
      for i in range(len(a)-1,-1,-1):
         alp[a[i]]+=j
         j*=10
   alp=sorted(alp.items(), key=operator.itemgetter(1), reverse=True)

   idx=9
   for a in alp:
      res[a[0]]=idx
      idx-=1

   ans=0
   for a in arr:
      tmp=''
      for b in a:
         tmp +=str(res[b])
      ans+=int(tmp)
   
   print(ans)