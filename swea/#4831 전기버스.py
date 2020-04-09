#4831 전기버스

T = int(input())
for TC in range(1, T+1):
    k,n,m = map(int,input().split())
    arr = list(map(int, input().split()))
    stop = []
    for i in range(200):
        stop.append(0)
    for i in range(m):
        stop[arr[i]] = 1
    
    j=0
    pos_org = 0
    pos2 = k
    cnt = 0
    while 1:
        if pos2 >= n:
            print("#%d %d" %(TC, cnt))
            break

        if stop[pos2] == 1:
            cnt+=1  #Find the Gas station
            pos_org = pos2
            pos2 += k
        else:
            pos2 -= 1 #backstep
            if pos2 == pos_org:#We can not arrive
                print("#%d %d" %(TC, 0))
                break    