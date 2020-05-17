#10250 ACM 호텔

a = int(input())

for _ in range(a):
    h,w,n = map(int,input().split())
    a = str((n-1)//h + 1)
    b = str(n%h)
    if b == '0':
        b = str(h)
    print(b+ a.rjust(2,'0'))
