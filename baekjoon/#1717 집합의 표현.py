#1717 집합의 표현

'''
disjoint-set, Union-Find 문제

사실 구현하는 로직을 이해하고 있다면 간단하게 풀 수 있는 문제지만, 로직 자체가 막 익숙하지는 않다는 것...

https://gmlwjd9405.github.io/2018/08/31/algorithm-union-find.html
아주 설명을 잘해주신다.

쉽게말하면 
시작할때 초기화 상태는 각각 root 즉, parent root 가 자신이다.

만약 a이랑 b를 union 하고 싶다.
그렇다면 a와 b의 parent root를 찾는다.
그 다음 b의 parent root에 a의 parent root를 연결시키면된다.

이렇게 말로 표현하니깐 좀 이해가 잘 안될 수 도 있는데 그림으로 그려보면서 이해하면 좋을 것 같다.


disjoint-set 에 대한 문제들을 더 풀어봐야겠다 !!
'''

import sys
import math
from collections import deque
import copy
input=sys.stdin.readline
INF=sys.maxsize

def find(parent,n):
    tmp=n
    while 1:
        if parent[tmp]==tmp:#루트를 찾음
            return tmp
        tmp=parent[tmp]

if __name__ == "__main__":
    n,m=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(m)]
    parent=[i for i in range(0,n+1)]

    for val in arr:
        a,b=val[1],val[2]
        if val[0]==0:
            parent[find(parent,b)]=find(parent,a)
        else:
            if find(parent,a)==find(parent,b):
                print('YES')
            else:print('NO')
