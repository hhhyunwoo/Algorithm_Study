#11727 2×n 타일링 2
N = int(input())

arr = [0 for _ in range(1001)]
arr[1] = 1
arr[2] = 3
for i in range(3,N+1):
    arr[i] = arr[i-1] + 2* arr[i-2]
print(arr[N] % 10007)
    
