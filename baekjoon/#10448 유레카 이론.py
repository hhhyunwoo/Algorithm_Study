#10448 유레카 이론

def dfs(cnt, num, SUM):
    global flag
    if cnt >= 3: #basis case
        if SUM == num:
            #print(1)
            flag = 1
        else:
            return

    i = 1
    while 1:
        SUM += T[i]
        if SUM > num:return
        dfs(cnt+1, num, SUM)
        SUM -= T[i]
        i += 1


N = int(input())
T = [0 for _ in range(51)]
T[1] = 1
for i in range(2,51):
    T[i] = T[i-1] + i

for i in range(N):
    flag = 0
    num = int(input())
    dfs(0,num, 0)
    if flag == 1: print(1)
    else : print(0)