#1021 회전하는 큐

n,m = map(int,input().split())
arr = list(map(int,input().split()))
q = [0]*n
j=1
for i in range(0,len(arr)):
    q[arr[i]-1] = j
    j+=1

answer = 0
target = 1
while 1:
    if sum(q)!=0:
        front,rear = 0,0
        idx = 0
        while 1:
            if q[idx]==target:
                front = idx
                break
            idx+=1

        idx=len(q)-1
        cnt = 1
        while 1:
            if q[idx]==target:
                rear=cnt
                break
            idx-=1
            cnt+=1
        if front<rear:
            tmp =[]
            tmp.extend(q[front:])
            tmp.extend(q[:front])
            q=tmp
            q.pop(0)
            answer += front
        else:
            tmp =[]
            tmp.extend(q[len(q)-rear:])
            tmp.extend(q[:-rear])
            q=tmp
            q.pop(0)
            answer += rear
        target += 1
    else:
        print(answer)
        break

#[1, 0, 0, 1, 0, 0, 0, 1, 0, 0, ]