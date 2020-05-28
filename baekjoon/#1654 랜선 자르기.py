#1654 랜선 자르기

if __name__ == "__main__":
    k,n = map(int,input().split())
    arr = [int(input()) for _ in range(k)]
    answer = 0
    front,rear=1,sum(arr)//n
    while front<=rear:
        mid = (front+rear)//2
        tmp = 0
        for a in arr:
            tmp += a//mid
        if tmp>=n:
            answer = mid
            front = mid+1 
        else:
            rear = mid-1

    print(answer)