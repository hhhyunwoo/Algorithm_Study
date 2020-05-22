#2164 카드2
from collections import deque

n = int(input())
arr = deque()
for i in range(1,n+1):
    arr.append(i)
if n == 1:
    print(1)
else:
    while 1:
        arr.popleft()
        if len(arr)==1:
            print(arr[0])
            break
        tmp = arr.popleft()
        arr.append(tmp)
