#11725 트리의 부모 찾기

import sys
sys.setrecursionlimit(10**9)

def check(val,pre,arr):
    global res
    if pre in arr[val]:
        arr[val].remove(pre)
    if not arr[val]: return
    for a in arr[val]:
        res[a] = val
        check(a,val,arr)


n = int(sys.stdin.readline())
arr = {i:[] for i in range(1,n+1)}
res = {i:[] for i in range(1,n+1)}

for _ in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

check(1,1,arr)
for i in range(2,n+1):
    print(res[i])