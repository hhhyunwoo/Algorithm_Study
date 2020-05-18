#2750 수 정렬하기

n = int(input())
arr = [int(input()) for _ in range(n)]
arr = sorted(arr)

for a in arr:
    print(a)