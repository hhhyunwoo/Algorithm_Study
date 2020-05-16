#2908 상수

a,b = map(str,input().split())
a=int(a[::-1])
b=int(b[::-1])
print(max(a,b))
