#2480 주사위 세게
arr = list(map(int,input().split()))

if arr.count(arr[0]) == 1:
    if arr.count(arr[1]) == 2: #2개 동일
        print(1000+arr[1]*100)
    else: #다다름
        print(max(arr)*100)
elif arr.count(arr[0]) == 2:
    print(1000+arr[0]*100)
else:
    print(10000+arr[0]*1000)
        