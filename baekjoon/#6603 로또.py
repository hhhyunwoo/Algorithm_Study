#6603 로또
from itertools import combinations

while 1:
    arr = list(map(int,input().split()))
    if arr[0] == 0: break

    N = arr[0]

    arr = arr[1:]
    for val in combinations(arr,6):
        print(*val)
    print("")