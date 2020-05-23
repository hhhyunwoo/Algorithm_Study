#10451 순열 사이클

import copy

t = int(input())
for _ in range(t):
    res = 0
    n = int(input())
    arr = dict()
    val = list(map(int,input().split()))
    for i in range(1,n+1):
        arr[i]= val[i-1]

    check = [0]*(n+1)
    check[0] = 1
    for i in range(1,n+1):
        if check[i] ==0:
            check[i] = 1
            visited=[i]
            cur = arr[i]
            while 1:
                if cur in visited:
                    res += 1
                    break
                visited.append(cur)
                check[cur] = 1
                cur = arr[cur]
                if cur == i:
                    res += 1
                    break
    print(res)
'''
2
8
3 2 7 8 1 4 5 6
10
2 1 3 4 5 6 7 9 10 8
'''