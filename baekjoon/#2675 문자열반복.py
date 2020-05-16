#2675 문자열반복
n = int(input())
for _ in range(n):
    a,b = map(str,input().split())
    tmp = ""
    for i in range(0,len(b)):
        tmp +=b[i]*int(a)
    print(tmp)