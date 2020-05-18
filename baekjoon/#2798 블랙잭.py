#2798 블랙잭

from itertools import combinations

n,m = map(int,input().split())
arr = list(map(int,input().split()))

dif= 9999999999
answer = 0
for val in combinations(arr,3):
    if sum(val) <= m:
        if dif > m-sum(val):
            dif = m-sum(val)
            answer = sum(val)
print(answer)
