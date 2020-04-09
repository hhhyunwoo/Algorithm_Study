#4835 구간합구하기

T = int(input())
for TC in range(1, T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))

    i = 0
    min = 9999999
    max = -9999999
    while 1:
        sum = 0
        if i+M > N:
            break
        for j in range(i,i+M):
            sum += arr[j]
        if sum>max:
            max = sum
        if sum < min:
            min = sum
        i += 1

    print('#%d %d' %(TC, max-min))
