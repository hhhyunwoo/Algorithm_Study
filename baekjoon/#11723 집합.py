#11723 집합

#리스트 뺏다 넣었다 계속해서 메모리 초과??
#그럼 visited 형식으로 진행해볼까

# ㄴㄴ 파이썬으로 안되는듯 다른사람들 코드도 다 안됨
import sys

N = int(input())
arr = dict()
for i in range(1,21):
    arr[i] = 0
ans = list()

for _ in range(N):
    com = list(map(str,sys.stdin.readline().split()))
    if len(com) >= 2:
        A = com[0]
        B = com[1]
    else:
        A = com

    if A == "add":
        arr[int(B)] = 1

    elif A == "remove":
        arr[int(B)] = 0

    elif A == "check":
        if arr[int(B)] == 1:
            ans.append(1)
        else:
            ans.append(0)

    elif A == "toggle":
        if arr[int(B)] == 1:
            arr[int(B)] = 0
        else:
            arr[int(B)] = 1
    
    elif A == "all":
        for i in range(1,21):
            arr[i] = 1

    elif A == "empty":
        for i in range(1,21):
            arr[i] = 0

for i in range(len(ans)):
    print(ans[i])