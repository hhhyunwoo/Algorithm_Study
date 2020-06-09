#1717 집합의 표현

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
