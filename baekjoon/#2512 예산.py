#2512 예산

input()
arr=list(map(int,input().split()))
m=int(input())
answer=-99999
front,rear = 0,max(arr)

while rear>=front:
    mid = (front+rear) //2
    res=0
    for a in arr:
        if a>mid:
            res+=mid
        else:
            res+=a
    if res > m:
        rear = mid-1
    else:
        answer=mid
        front = mid+1

print(answer)