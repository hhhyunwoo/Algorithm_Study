'''#10972 다음 순열

#실패
#next_permutaion을 구현해야한다.

from itertools import permutations

N = int(input())
arr = list()
ans = list(map(int,input().split()))
for i in range(1,N+1):
    arr.append(i) 

flag =0
for val in permutations(arr,N):
    if flag == 1:
        ANSWER = val
        flag = -1
        break
    
    cnt = list(val)
    if cnt == ans:
        flag = 1

if flag != -1:
    print(-1)
else:print(*ANSWER)'''