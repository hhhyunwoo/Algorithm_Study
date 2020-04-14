#1182 부분수열의 합

from itertools import combinations

N, S = map(int,input().split())

arr = list(map(int,input().split()))
cnt =0

for i in range(1,N+1):
    for val in combinations(arr,i):
        if S == sum(val):
            cnt +=1
print(cnt)