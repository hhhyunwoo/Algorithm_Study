#1547 공

m = int(input())
arr = [list(map(int,input().split())) for _ in range(m)]
res = 1
for a in arr:
    if res in a:
        if a[0] == res:
            res = a[1]
        else:
            res = a[0]
print(res)