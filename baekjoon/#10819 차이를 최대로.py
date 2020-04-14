#10819 차이를 최대로

from itertools import permutations

def cal(arr):
    S = 0
    for i in range(0,len(arr)-1):
        S += abs(arr[i] - arr[i+1])
    return S

N = int(input())
arr = list(map(int,input().split()))
SUM = -9999
for val in permutations(arr,N):
    calculate = cal(val)
    SUM = max(SUM,calculate)
print(SUM)