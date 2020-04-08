#9095
T = int(input())
arr = [0 for _ in range(13)]
arr[1] =1
arr[2] = 2
arr[3] = 4
for TC in range(T):
    N = int(input())
    for i in range(4, N+1):
        arr[i] = arr[i-3] + arr[i-2] + arr[i-1]
    print(arr[N])