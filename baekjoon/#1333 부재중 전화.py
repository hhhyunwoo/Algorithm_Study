#1333 부재중 전화
#하 어렵노!

n,l,d = map(int,input().split())
arr = []
tmp = l
ring = d
flag = 0
for i in range(1,n+1):
    arr.append([l*i+5*(i-1),l*i+5*i])
#a[0]<=  <a[1]
flag = 0
while 1:
    for a in arr:
        if a[0]<=ring<a[1]:
            print(ring)
            flag = 1
            break
        if a[1] > ring:
            ring += d
            break
    if flag ==1:
        break
    if ring >= arr[len(arr)-1][0]:
        print(ring)
        break