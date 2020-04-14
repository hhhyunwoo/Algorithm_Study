#10971 외판원 순회2
#MIN 값 너무 낮게 줘서 틀렸음.,,.

from itertools import permutations

def cal(arr):
    sum = 0
    for i in range(0,len(arr)-1):
        if MAP[arr[i]][arr[i+1]] == 0:#못가는 경우
            return -1
        sum += MAP[arr[i]][arr[i+1]]

    if MAP[arr[len(arr)-1]][arr[0]] == 0:#못가는 경우
        return -1
    sum += MAP[arr[len(arr)-1]][arr[0]]
    return sum

N = int(input())

MAP = [list(map(int,input().split()))for _ in range(N)]

arr = list()
MIN = 99999999999
for i in range(0,N):
    arr.append(i)
for val in permutations(arr,N):
    ans = cal(val)
    if ans == -1: continue
    MIN = min(MIN, ans)

print(MIN)