#1850 최대공약수

def gcd(a,b):
    while b != 0:
        tmp = a%b
        a = b
        b = tmp
    return a

A,B = map(int,input().split())
answer = gcd(A,B)
ans = ""
for i in range(answer):
    ans+='1'
print(ans)