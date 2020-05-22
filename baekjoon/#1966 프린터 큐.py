#1966 프린터 큐

from collections import deque

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    q1 = list(map(int,input().split()))
    q2=[0]*n
    q2[m] = 1

    cnt = 0
    while 1:
        tmp = q1[0]
        flag = 0
        for i in range(1,len(q1)):
            if q1[i]>tmp:
                flag = 1
                break
        if flag == 1:
            tmp = q1.pop(0)
            q1.append(tmp)

            tmp = q2.pop(0)
            q2.append(tmp)
        else:
            q1.pop(0)
            tmp = q2.pop(0)
            cnt +=1
            if tmp == 1:
                print(cnt)
                break