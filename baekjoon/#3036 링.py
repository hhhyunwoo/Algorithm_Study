#3036 링

n = int(input())
arr = list(map(int,input().split()))

for i in range(1,len(arr)):
    a = arr[0]
    idx = arr[i]
    while 1:
        if arr[i]%idx == 0 and a%idx == 0:
            print(str(a//idx)+'/'+str(arr[i]//idx))
            break
        else:
            idx-=1

        