#1476 날짜 계산

E, S, M = map(int,input().split())
cnt = 0
i,j,k = 1,1,1
while 1:
    cnt += 1
    if i==E and j==S and k == M:
        print(cnt)
        break
    i += 1
    j += 1
    k += 1
    if i >15:
        i = 1
    if j > 28:
        j = 1
    if k > 19:
        k = 1
