re_#2003 수들의 합2

#투포인터
https://m.blog.naver.com/kks227/220795165570

N,M = map(int,input().split())

arr = list(map(int,input().split()))

i,j=0,0
cnt = 0
sum = 0
while 1:
    if sum >= M:
        sum -= arr[i]
        i += 1
    elif j>=N: break
    else:
        sum += arr[j]
        j += 1
    if sum == M:
        cnt += 1
print(cnt)