#10974 모든순열

from itertools import permutations

N = int(input())
arr = list()
for i in range(1,N+1):
    arr.append(i)

for val in permutations(arr,N):
    print(*val)