#1057 토너먼트

n,c,d = map(int,input().split())
a = max(c,d)
b = min(c,d)
res = 1
while 1:
    if a%2==0:
        if a-1 == b:
            print(res)
            break
        a//=2
    else:
        a=(a+1)//2
    if b%2==0:
        b//=2
    else:
        b=(b+1)//2

    res += 1